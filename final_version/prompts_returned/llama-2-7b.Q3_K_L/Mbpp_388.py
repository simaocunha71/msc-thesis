"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
# Solution 1:
def highest_power_of_2 (n): 
    if n == 0:  
        return 0

    elif n%2 == 1:  # If the number is odd, then it cannot be a power of 2
        return None
    
    else:              # Otherwise, check with a while loop
        i = 1
        j = 3

        while (i <= j):  # Keep incrementing from both sides until you find the highest power of 2 less than or equal to n
            if n % i == 0:      # If the number is divisible by i, then add it to the list
                return i
            else:              # Otherwise, continue with the next value in the list: j 
                i += 1
                j = (i + 2) // 4
    
print(highest_power_of_2(30))