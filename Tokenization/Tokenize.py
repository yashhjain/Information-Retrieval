# Author: Yash Hemant Jain
# Net Id: yxj180004
# CS 6322.001 Information Retrieval

import glob
import re
import sys
from collections import Counter
import collections
from datetime import datetime
from Stemming import PorterStemmer

start=datetime.now()    # Code Execution Start Time

##----------------TOKENIZATION---------------------##

count=0
j=0
token=[]

#path = 'Cranfield//*'
#path = '//people//cs//s//sanda//cs6322//Cranfield//*'

path=sys.argv[1]+'/*'
files=glob.glob(path)

for file in files:
    f=open(file, 'r')
    words=f.read()
    text = re.sub(r'<.*?>',"", words)   # Removes SGML Tags
    txt = re.sub(r'[,-]'," ", text)     # Removes comma and hyphen, replaces with space
    txt1 = re.sub(r'[^\w\s]','',txt)    # Removes punctuation marks
    res = re.sub(r'[^A-Za-z]'," ",txt1) # Removes numbers and special characters
    res1=res.lower()                    # Lower-case the tokens
    tokens=res1.split()
    token.extend(tokens)
    if(len(tokens)>0):
        #print(tokens)
        count+=len(tokens)
    f.close()

unique=set(token)   # Identifies the unique tokens

w1=Counter(token)   # Identifies the tokens which occured only once
for i in token:
    if w1[i]==1:
        once=1
        j+=1
    else:
        once=0

print("##----------------TOKENIZATION---------------------##")
print("Number of tokens:",count)
print("Number of unique words:",len(unique))
print("Number of words that occured only once:",j)

print("30 most frequent words in the Cranfield text collection (word,frequency):")
freq=collections.Counter(token).most_common(30) #Identifies the 30 most frequent tokens
for i in freq:
    print(i)


print("Average number of word tokens per document:",round(count/len(files)))

stop=datetime.now()     # Code Execution End Time
print("Time the program took to acquire the text characteristics:")
print(stop-start)

##----------------STEMMING----------------------##

k=0
c=0
pslist=[]
ps=PorterStemmer()  # Uses PorterStemmer class defined in Stemming.py
for i in token:
    pslist.append(ps.stem(i,0,len(i)-1))
    c+=1
#print(set(pslist)) # Identifies the unique stems

print("##----------------STEMMING---------------------##")
print("Number of distinct stems in the Cranfield text collection:",len(set(pslist)))

w2=Counter(pslist)  # Identifies the stems which occured only once
for i in pslist:
    if w2[i]==1:
        once=1
        k+=1
    else:
        once=0
print("Number of stems that occur only once in the Cranfield text collection:",k)

print("30 most frequent stems in the Cranfield text collection (stem,frequency):")
freq1=collections.Counter(pslist).most_common(30)   #Identifies the 30 most frequent stems
for i in freq1:
    print(i)

print("Average number of word stems per document:",round(len(set(pslist))/len(files)))
