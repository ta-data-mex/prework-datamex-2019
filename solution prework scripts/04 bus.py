# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:41:31 2019

@author: luisf
"""

"""
04 bus
"""

stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

# 1. Calculate the number of stops.
print(len(stops))

# 2. Assign a variable a list whose elements are the number of passengers in each stop: 
# Each item depends on the previous item in the list + in - out.

number_passengers_per_stop = []
passengers_count = 0 

for i, j in stops:
    subtraction = (i-j)
    passengers_count += subtraction
    number_passengers_per_stop.append(passengers_count)
    
    
print(number_passengers_per_stop)

# 3. Find the maximum occupation of the bus.
max(number_passengers_per_stop)

# 4. Calculate the average occupation. And the standard deviation.
import numpy as np

print(np.mean(number_passengers_per_stop))
print(np.std(number_passengers_per_stop))
