# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:55:42 2019

@author: luisf
"""

"""
06. snail and well
"""

# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance

well_height = 125
daily_advance = 30
night_retreat = 20
accumulated_distance = 0

# Assign 0 to the variable that represents the solution
days = 0

# Write the code that solves the problem

while accumulated_distance < well_height:
    accumulated_distance = accumulated_distance + daily_advance
    if accumulated_distance > well_height:
        days += 1
        break
    accumulated_distance = accumulated_distance - night_retreat
    days += 1

# Print the result with print('Days =', days)

print("Days =", days)

############################################################
################      BONUS  ###############################
############################################################
days_bonus = 0
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
accumulated_distance = 0
night_retreat = 20
well_height = 125

while accumulated_distance < well_height:
    for i in advance_cm:
        accumulated_distance = accumulated_distance + i
        if accumulated_distance > well_height:
            days_bonus += 1
            break
        accumulated_distance = accumulated_distance - night_retreat
        days_bonus += 1

print("Days Bonus =", days_bonus)

# What is its maximum displacement in a day? And its minimum?
print("Maximum displacement in a day:",max(advance_cm),"\nMinimum displacement in a day:", min(advance_cm))

# What is its average progress?
import numpy as np
np.mean(advance_cm)

# What is the standard deviation of your displacement during the day?
np.std(advance_cm)
