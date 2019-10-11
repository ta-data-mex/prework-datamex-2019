# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:28:33 2019

@author: luisf
"""

"""
05. mission impossible
"""

dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]

# Show volumes that exceed 10 dBs

greater_than10_dbs = []

for i in dbs:
    if i > 10:
        greater_than10_dbs.append(i)
        
print(greater_than10_dbs)

# Show the moments (indexs of the list) in which a volume exceeds 10 dBs

index_greater_than10_dbs = []

for n,i in enumerate(dbs):
    if i > 10:
        index_greater_than10_dbs.append(n)
        
print(index_greater_than10_dbs)

# Combine the last two exercises to show the moments when a 
# volume exceeds 10 dBs. HINT: Use the enumerate function

all_greater_than10 = []

for n, i in enumerate(dbs):
    if i > 10:
        all_greater_than10 += [(n,i)]
        
print(all_greater_than10)

# Ethan is discovered if two consecutive volumes are greater than 10 dB. Is he safe? 
# HINT: Beware of the extremes, do not have an error of the type
# IndexError: list index out of range

def count_consecutives(listt):
    count_of_consecutives = []
    count = 1
    for i in range(len(listt[:-1])):
            if listt[i]+1 == listt[i+1]:
                count+=1
            else:
                count_of_consecutives.append(count)
                count=1
    count_of_consecutives.append(count)
    return count_of_consecutives

count_consecutives(dbs)

if any(i >=2  for i in (count_consecutives(dbs))):
    print("Alarm!")

#La diferencia para evitar IndexError:   
#range(len(index_greater_than10_dbs[:-1]))
#range(len(index_greater_than10_dbs))
    
#BONUS
post_hacking = []

for i in dbs:
    if (i > 20 and i < 30):
        post_hacking.append(i-12)
    elif i > 30:
        post_hacking.append(i-18)
    else: 
        post_hacking.append(i)

print(dbs)
print(post_hacking)

