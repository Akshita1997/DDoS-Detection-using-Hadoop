#!/usr/bin/python
import sys

a =[]
wordcount ={}

for line in sys.stdin:
    line = line.strip()
    words = line.split("\n")
    
    for ips in words:
	a.append(ips[2])

for word in a:
    if word not in wordcount:
	wordcount[word] = 1
    else:
	wordcount[word] += 1
print(wordcount)
