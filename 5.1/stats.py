# 1. split reddit corpus into one document = one file
import os
import sys
import uuid

dir = './data/'
print '> Splitting Reddit corpus to one document per file (if required)'
for file in os.listdir(dir):
    # only reddit corpus files starts with 'corpus_'
    if file.startswith('corpus'):
        doc = open(dir + file, 'r').read()
        # every new line represents one document
        for line in doc.splitlines():
            temp = line.replace(" ", "")
            if temp:
                newfile = open(dir + str(uuid.uuid4()) + '.txt', 'w')
                newfile.write(line)
                newfile.close()
        print 'Deleting ', dir + file
        # delete file once splitting completes
        os.remove(dir + file)


# 2. get corpus statistics
import nltk

print '> Calculating statistics now, please wait'
corpusReader = nltk.corpus.PlaintextCorpusReader(dir, '.*\.txt', encoding='latin-1')
print 'The number of sentences =', len(corpusReader.sents())
print 'The number of tokens =', len([word for sentence in corpusReader.sents() for word in sentence])
print 'The number of type =', len(set(corpusReader.words()))
