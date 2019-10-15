# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:32:43 2019

@author: luisf
"""

"""
08. robin hood
"""

points = [(4, 5), (0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

# 1. Robin Hood is famous for hitting an arrow with another arrow. Did you get it?

#list([x for x in points if points.count(x) > 1])
#set([x for x in points if points.count(x) > 1])
points.count((4,5))

#la función set te crea un elemento distinct,donde no hay repetidos.
#el ciclo en unión con el count hacen que se cuenten los elementos repetidos en la lista points.
if len(set([x for x in points if points.count(x) > 1])) >= 1:
    print(True)


# 2. Calculate how many arrows have fallen in each quadrant.

#first_quadrant = []
#second_quadrant = []
#third_quadrant = []
#fourth_quadrant = []

count_first_quadrant = 0
count_second_quadrant = 0
count_third_quadrant = 0
count_fourth_quadrant = 0

for x,y in points:
    if(x > 0 and y > 0):
        count_first_quadrant += 1
    elif(x < 0 and y > 0):
        count_second_quadrant += 1      
    elif(x < 0 and y < 0):
        count_third_quadrant += 1
    elif(x > 0 and y < 0):
        count_fourth_quadrant += 1
print((count_first_quadrant, count_second_quadrant, count_third_quadrant, count_fourth_quadrant))


#len(first_quadrant)
#len(second_quadrant)

# 3. Find the point closest to the center. Calculate its distance to the center
# Defining a function that calculates the distance to the center can help.

closet_to_origin = [(x,y) for x,y in points if abs(x)+abs(y) == 2]
#####Distance to the center  
distance_to_origin = [abs(x)+abs(y) for x,y in points]
#print(distance_to_origin)
print(closet_to_origin,'\n',float(min(distance_to_origin)))


# 4. If the target has a radius of 9, calculate the number of arrows that 
# must be picked up in the forest.

radious_nine = [(x,y) for (x,y) in points if abs(x) == 9 or abs(y) == 9]
print(radious_nine,'\n', len(radious_nine))

