"""
PREWORK IRONHACK DATA ANALYTICS
"""

#Loops
KF_SexAppeal = {'Caro': ":)", 'Fer':90, 'Edna':60, 'Delia':50}

for name, sexappeal in KF_SexAppeal.items():
    print("La atracción que siento por", name, "es igual a", sexappeal)


##########################################################################
##########################################################################
    
total_time = 60
minutes_elapsed = 0
wait = 15

print("Cake is in the oven.")
#minutes_elapsed += wait
#print(minutes_elapsed)

while minutes_elapsed < total_time:
    print("Cake is not done yet.")
    minutes_elapsed += wait

print("It's done. Let's eat cake!")

##########################################################################
##########################################################################

#Files in Python

import os

os.getcwd()

os.chdir('/Users/luisf/Desktop')

#Creando un txt
with open("ejemplo.txt", "w") as f:
    f.write("Hello World! \n")
    f.write("khe asiendo? \n")
    f.write("nachoss")
    
#Leyendo
with open("ejemplo.txt", "r") as f:
    ejemplo = f.readlines()
    for i in ejemplo:
        print(i)
        
#Abrir un CSV

"""
RUTA --- /d/Documentos/Python for Data Projects
"""
data = []

with open("D:/Documentos/Python for Data Projects/weight_height.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split()[0].split(","))

###Analisis
        
heights = []

for person in data[1:]:
    height = int(person[2]) #Aca el número es 2 porque se refiere a la columna del csv o lista que importamos
    heights.append(height)

avg_height = sum(heights)/len(heights)
print(avg_height)