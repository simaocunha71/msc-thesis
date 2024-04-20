"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
import math
def power_base_sum(base:int= 1,power:int= 1):
    """Returns number of times to add base if power is even or power/2 plus 1 if power is odd."""
    result = 0
    for i in range (power // 2 +1 , 0,-1):
        result += math.pow(base,i)
        
    return result
    
# Driver code
print("value of the function: ", power_base_sum(2,3))