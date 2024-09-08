def max_Product(arr):
    arr.sort() # Sort the array in ascending order
    return (arr[-1], arr[-2]) # Return the last two elements as they are the highest

print(max_Product([1,2,3,4,7,0,8,4])) # (7, 8)

"""
The function works by first sorting the array in ascending order. 
The largest pair product will be obtained by multiplying the two largest numbers in the sorted array (which will be at the end of the array). 
So, it returns the last two elements of the sorted array.
"""

# Time complexity: O(n log n)
# Space complexity: O(1)
<jupyter_output>
(7, 8)
<jupyter_text>
Method 2:
<jupyter_code>
def max_Product(arr):
    max_num1 = max_num2 = float('-inf') # Initialize two variables to negative infinity
    for num in arr: # Iterate over the array
        if num > max_num1: # If the current number is greater than max_num1
            max_num2 = max_num1 # max_num2 takes the value of max_num1
            max_num1 = num # max_num1 takes the value of the current number
        elif num > max_num2: # If the current number is not greater than max_num1 but greater than max_num2
            max_num2 = num # max_num2 takes the value of the current number
    return (max_num1, max_num2) # Return the two numbers

print(max_Product([1,2,3,4,7,0,8,4])) # (8, 7)

"""
The function works by maintaining two variables max_num1 and max_num2 to store the two largest numbers. 
It then iterates over the array. If the current number is greater than max_num1, max_num2 is updated with the value of max_num1 and max_num1 is updated with the current number. 
If the current number is not greater than max_num1 but greater than max_num2, then max