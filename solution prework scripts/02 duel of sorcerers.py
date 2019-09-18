# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:12:24 2019

@author: luisf
"""

"""
02. duel of sorcerers
"""

sequence = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

gandalf_wins = 0
saruman_wins = 0

for i in range(len(sequence)):
    if gandalf[i] > saruman [i]:
        gandalf_wins += 1
        print("The", sequence[i], "duel is won by Gandalf:", gandalf[i], "againts", saruman[i],", wins", gandalf[i])
    else:
        saruman_wins += 1
        print("The", sequence[i], "duel is won by Saruman:", gandalf[i], "againts", saruman[i],", wins", saruman[i])
print("Total Gandalf wins:", gandalf_wins)
print("Total Saruman wins:", saruman_wins)
if gandalf_wins > saruman_wins:
    print("Gandalf wins the duel")
elif gandalf_wins == saruman_wins:
    print("The duel is a tie")
else: 
    print("Saruman wins the duel")


 
    