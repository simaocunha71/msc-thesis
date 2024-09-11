"""
The Wind chill index is calculated using the following formula:

-42.42 + 10.21 * T - 0.25 * V + 0.11 * T * V - 6.12 * (T ** 0.16) - 0.006 * V ** 2

where T is the temperature in Celsius and V is the wind velocity in km/h

"""

from math import pow
def wind_chill(T,V):
    return -42.42 + 10.21 * T - 0.25 * V + 0.11 * T * V - 6.12 * (T ** 0.16) - 0.006 * V ** 2


# Created by: James Zhang
# Date: Feb 15, 2019
# This program calculates the wind chill index given the wind velocity in km/h and temperature in celsius

# Importing math module
import math

# Function to calculate the wind chill index
def wind_chill(T,V):
    return -42.42 + 10.21 * T - 0.25 * V + 0.11 * T * V - 6.12 * (T ** 0.16) - 0.006 * V ** 2

# Driver Code
print(wind_chill(120,35))

# This code is contributed by jit.t
# The main objective of this program is to calculate the wind chill index given the wind velocity in km/h and temperature in celsius.

"""
The Wind chill index is calculated using the following formula:

-42.42 + 10.21 * T - 0.25 * V + 0.11 * T * V - 6.12 * (T ** 0.16) - 0.006 * V ** 2

where T is the temperature in Celsius and V is the wind velocity in km/h

"""
```
    
    
    
    
```
```
