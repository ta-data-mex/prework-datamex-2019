# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:56:32 2019

@author: luisf
"""

"""
07. lyrics
"""
babyshark = """Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…"""

print(babyshark)

#Step 1: First Paragraph
#Create a code to print the first paragraph and asign it to a variable. 

babyshark_1 = ""
count = 0
for i in babyshark:
    babyshark_1 += str(i)
    if i == "\n":
        count += 1
    if count == 4:
        break
print(babyshark_1)


#Step 2: Full song
#Create a code that prints the complete lyrics. 

result = ""
for i in range(len(babyshark)):
    result += babyshark[i]
print(result)

#Step 3: Check output
#Now i want you must create a string variable called result to store all the characters and check if it is equal to the lyrics. Remenber de hint section. 

print(result == babyshark)

#Step 4: Function
#Create a functions called babyshark() that generates the wanted output.

def baby_shark_lyrics(lyrics):
    result = ""
    for i in range(len(lyrics)):
        result += lyrics[i]
    return result

print(baby_shark_lyrics(babyshark) == babyshark)

#Step 5: Files
#Baby shark lyrics can be read in the songs folder. Try to store the content of that file in a variable called text and check if it is equal to the babyshark variable and the output of your baby_shark_lyrics function. 

text = open("baby-shark.txt", encoding='utf-8')
text = text.read()
#text = str(text)
print(text)

print(text == babyshark)
print(text == baby_shark_lyrics(babyshark))


#Step 6: Refactor
#Now I want you to refactor your baby_shark_lyrics function in order to be less than 400 characters. If your code is larger than 400 characters, you should change baby_shark_lyrics function in order to shorten it.

import inspect

code = inspect.getsource(baby_shark_lyrics)

print('Your baby_shark_lyrics functions has {} characters'.format(len(code)))
print(len(code) < 400)

#Bonus

#Step 1. Create bottles_lyrics function

def bottles_lyrics(lyrics):
    result = ""
    for i in range(len(lyrics)):
        result += lyrics[i]
    return result

bottles_lyrics(text_2)

#Step 2. Open file

text_2 = open("99-bottes-of-beer.txt")
text_2 = text_2.read()
print(text_2)

print(text_2 == bottles_lyrics(text_2))

#Step 3: Check code

code = inspect.getsource(bottles_lyrics)

print('Your bottles_lyrics functions has {} characters'.format(len(code)))
print(len(code) < 1000)