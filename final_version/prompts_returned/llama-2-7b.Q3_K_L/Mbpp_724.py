"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""

def power_base_sum(base,power):
    """ Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power. assert power_base_sum(2,100)==115  """

    if (power == 0):
        return 0
    
    elif (power < 0):
        return int("inf")

    else:
        sum = 0
        
        while (base >= 2**power):
            sum += base % 10  
            
            base //= 10
            
        return sum
