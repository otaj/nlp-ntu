import os
import uuid
import shutil
import nltk
import re

##### Function to filter out unwanted posts and tweets #####

try:
    # UCS-4
    emojiRe = re.compile(u'[U00010000-U0010ffff]')
except re.error:
    # UCS-2
    emojiRe = re.compile(u'[uD800-uDBFF][uDC00-uDFFF]')

def filterReddit(sentence):
    text = re.sub(r'^>+[ .]*$', '', sentence).replace('  ', ' ') # quote
    text = re.sub(r'[*^]+', '', text).replace('  ', ' ') # superscript
    text = re.sub(r'^\[.+\]\(.+\)$', '', text).replace('  ', ' ') # hyperlink
    emojiRe.sub('', text).replace('  ', ' ') # emoji
    return text

def filterTwitter(sentence):
    text = re.sub(r'http\S+', '', sentence).replace('  ', ' ') #url
    emojiRe.sub('', text).replace('  ', ' ') # emoji
    return text

########################################

##### Consolidate all crawling data #####

if not os.path.exists('data'):
    os.makedirs('data')

filenames = ['reddit-crawler/data/hilary.txt', 'twitter-crawler/data/hilary.txt']
with open('data/hilary.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            if (fname == 'reddit-crawler/data/hilary.txt'):
                text = filterReddit(infile.read())
            else:
                text = filterTwitter(infile.read())
            
            if (text):
                outfile.write(text)

filenames = ['reddit-crawler/data/trump.txt', 'twitter-crawler/data/trump.txt']
with open('data/trump.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            if (fname == 'reddit-crawler/data/trump.txt'):
                text = filterReddit(infile.read())
            else:
                text = filterTwitter(infile.read())
            
            if (text):
                outfile.write(text)

# Split the documents into separate files

if not os.path.exists('data/hilary'):
    os.makedirs('data/hilary')
for line in open('data/hilary.txt', 'r').read().splitlines():
    temp = line.replace(" ", "")
    if temp:
        newfile = open('data/hilary/' + str(uuid.uuid4()) + '.txt', 'w')
        newfile.write(line)
        newfile.close()

if not os.path.exists('data/trump'):
    os.makedirs('data/trump')
for line in open('data/trump.txt', 'r').read().splitlines():
    temp = line.replace(" ", "")
    if temp:
        newfile = open('data/trump/' + str(uuid.uuid4()) + '.txt', 'w')
        newfile.write(line)
        newfile.close()

print '> Hilary'
hilaryCorpus = nltk.corpus.PlaintextCorpusReader('data/hilary/', '.*\.txt', encoding='latin-1')
print 'Number of sentences =', len(hilaryCorpus.sents())
print 'Number of tokens =', len([word for sentence in hilaryCorpus.sents() for word in sentence])
print 'Number of type =', len(set(hilaryCorpus.words()))
print 'Number of documents =', len(next(os.walk('data/hilary/'))[2])

print '\n> Trump'
trumpCorpus = nltk.corpus.PlaintextCorpusReader('data/trump/', '.*\.txt', encoding='latin-1')
print 'Number of sentences =', len(trumpCorpus.sents())
print 'Number of tokens =', len([word for sentence in trumpCorpus.sents() for word in sentence])
print 'Number of type =', len(set(trumpCorpus.words()))
print 'Number of documents =', len(next(os.walk('data/trump/'))[2])

########################################

#if os.path.exists('data'):
#    shutil.rmtree('data', ignore_errors=True)