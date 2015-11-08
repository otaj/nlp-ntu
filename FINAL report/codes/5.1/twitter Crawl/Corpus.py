import os

DIR = "data/txt/"
PATH = "data/corp.txt"

class Corpus:
    def __init__(self, dir, path):
        self.dir = dir
        self.path = path
        self.file = open(self.path, mode='w')

    def concat(self):
        for file in os.listdir(self.dir):
            self.file.write(open(os.path.join(self.dir,file), mode='r').read())
            self.file.write('\n')
        self.file.close()

if __name__ == '__main__':
    corp = Corpus(DIR, PATH)
    corp.concat()