#!/usr/bin/python3
"""reducer.py"""

import sys
import math
from operator import itemgetter

a=[]
wordcount={}
count=0
S=0
entropy=0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.split()

    try:
        #print(line[2] + "\t" + line[4] + "\t" + line[5])
        a.append(line[2])
        
    except:
        print("-")
print()

for word in a:
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1
for k,v in wordcount.items():
	print (k, v)
	count= count+1
	S=S+v

print()
print(S)
print(count)

for k,v in wordcount.items():
	entropy= entropy+ ((v/S)* (math.log(v/S,2)))

entropy= (-1)*entropy
print(entropy)

Normalized_entropy= (entropy/(math.log(count,2)))
print(Normalized_entropy)
print('\n\n')


    


    
    

                
           
        	
        	 



     
            



    



