Step 1: Labeled Data Collection from Twitter
Step 2: All the data stored in subfolder --- "txt"

For normal Data Preprocessing
Step 3: Ran normals.py
Step 4: The result stored in subfolder --- "normals"
Step 5: Converted "normals" subfolder into weka dataset by TextDirectoryLoader
Step 6: Acquired the "text_normals.arff" file
Step 7: Open "text_normals.arff" by Weka
Step 8: Click "Explorer" button
Step 9: In "Preprocess" tag -> Open file... -> Select "text_normals.arff"
Step 10: In "Classify" tag -> Choose Classifier "weka/classifiers/meta/Vote" 
-> Click "Start" button -> Generate Classifier output

For emoticons Data Preprocessing
Step 3: Ran emoticons.py
Step 4: The result stored in subfolder --- "emoticons"
Step 5: Converted "emoticons" subfolder into weka dataset by TextDirectoryLoader
Step 6: Acquired the "text_emoticons.arff" file
Step 7: Open "text_emoticons.arff" by Weka
Step 8: Click "Explorer" button
Step 9: In "Preprocess" tag -> Open file... -> Select "text_emoticons.arff"
Step 10: In "Classify" tag -> Choose Classifier "weka/classifiers/meta/Vote" 
-> Click "Start" button -> Generate Classifier output

Please refer to two PNG files --- "ListOfEmoticons" and "ListOfNormals"