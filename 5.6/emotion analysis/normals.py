import os, os.path, shutil

positive_texts_list = ['elated', 'overjoyed', 'enjoy', 'excited', 'proud', 'joyful',
                           'happy', 'blessed', 'amazing', 'wonderful', 'excelent', 'delighted',
                           'enthusiastic', 'calm', 'peace', 'silent', 'serene',
                           'consent', 'convince', 'satisfied', 'relax']
negative_texts_list = ['nervous', 'anxious', 'tension', 'afraid', 'fearful', 'distress',
                           'stress', 'angry', 'annoy', 'tense', 'bother', 'disturb',
                           'irritate', 'mad', 'furious', 'sad', 'sorrow', 'hapless', 'fatigue',
                           'gloomy', 'miserable', 'hopeless', 'depress', 'fatigued', 'unhappy',
                           'laugh', 'not']

path = './txt'
dest_pos_folder = './txt/positive/'
dest_neg_folder = './txt/negative/'
dest_und_folder = './txt/undefined/'

num_files = len([f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))])

print("The number of records is : ")
print(num_files)

#Main program file

my_list = [f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))]

for member in my_list:
    if member.endswith('.txt'):
        #print member
        process_pursuit_num = 0
        #1 -> positive
        #2 -> negative
        #0 -> undefined
        directory = path + "/" + member 
        #print directory
        with open(directory, "r") as myfile:
            data = myfile.read().replace('\n','')
            data_low = data.lower()
            #print data
            #print data_low
            for x in positive_texts_list:
                #print x
                if x in data_low:
                    #print 'success'
                    process_pursuit_num = 1
                    break
                else:
                    #print 'fail'
                    #break
                    continue
            if(process_pursuit_num != 1):
                for y in negative_texts_list:
                    #print y
                    if y in data_low:
                        #print 'sad'
                        process_pursuit_num = 2
                        break
                    else:
                        #print 'unsad'
                        #break
                        continue
            
        if(process_pursuit_num == 1):
            shutil.move(directory, dest_pos_folder)
        elif(process_pursuit_num == 2):
            shutil.move(directory, dest_neg_folder)
        else:
            shutil.move(directory, dest_und_folder)

        #print(process_pursuit_num)
    #break

#print positive_texts_list
#print negative_texts_list
print 'End of preprocess !!'

