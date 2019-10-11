# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:02:15 2019

@author: luisf
"""

"""
03. processor temperature
"""

# import
import matplotlib.pyplot as plt
%matplotlib inline

# axis x, axis y
y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day')

# assign a variable to the list of temperatures
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]

# 1. Calculate the minimum of the list and print the value using print()
min(temperatures_C)print(5+5)

# 2. Calculate the maximum of the list and print the value using print()
max(temperatures_C)

# 3. Items in the list that are greater than 70ºC and print the result
greater_than_70 = []

for i in temperatures_C:
    if i >= 70:
        greater_than_70.append(i)
print("Las temperaturas mayores a 70ºC son las siguientes:", greater_than_70)

# 4. Calculate the mean temperature throughout the day and print the result
mean = sum(temperatures_C) / len(temperatures_C)
print(mean)

# 5.1 Solve the fault in the sensor by estimating a value
temperatures_C_b = []

for i in temperatures_C:
    if i != 0:
        temperatures_C_b.append(i)

print(temperatures_C_b)

estimated_value = round(sum(temperatures_C_b) / len(temperatures_C_b),1)

#Interpolación: sacar un promedio de los valores de los lados de la posición.

# 5.2 Update of the estimated value at 03:00 on the list
temperatures_C[3] = estimated_value
print(temperatures_C)

# Bonus: convert the list of ºC to ºFarenheit
temperatures_F = []

for i in temperatures_C:
    temp = []
    temp = 1.8 * i + 32
    temperatures_F.append(temp)

print(temperatures_F)

#Comprensión de lista: un chavo utilizó esto.

# Print True or False depending on whether you would change the cooling system or not
if len(greater_than_70) > 4 or any(i > 80 for i in temperatures_C) or mean > 65:
    print(True)

#################################
### Future improvements
#################################
    
# 1. We want the hours (not the temperatures) whose temperature exceeds 70ºC
dictionary = dict(zip(x, temperatures_C))
print(dictionary)

hours_greater_70 = []

for x,y in dictionary.items():
    if y >= 70:
        hours_greater_70.append(x)
        
print(hours_greater_70)

# 2. Condition that those hours are more than 4 consecutive and consecutive, not simply the sum of the whole set. Is this condition met?

def count_consecutives(listt):
    count_of_consecutives = []
    count = 1
    for i in range(len(listt[:-1])): #lisst[:-1] en lugar de todo el len(listt) para evitar IndexError
            if listt[i]+1 == listt[i+1]:
                count+=1
            else:
                count_of_consecutives.append(count)
                count=1
    count_of_consecutives.append(count)
    return count_of_consecutives

count_consecutives(hours_greater_70)

if any(i > 4  for i in (count_consecutives(hours_greater_70))):
    print("Would I change the cooling system?: Yes!")

#La diferencia para evitar IndexError:   
#range(len(hours_greater_70[:-1]))
#range(len(hours_greater_70))

# 3. Average of each of the lists (ºC and ºF). How they relate?
import numpy as np

print(np.mean(temperatures_C),np.mean(temperatures_F))

# 4. Standard deviation of each of the lists. How they relate?
print(np.std(temperatures_C), np.std(temperatures_F))