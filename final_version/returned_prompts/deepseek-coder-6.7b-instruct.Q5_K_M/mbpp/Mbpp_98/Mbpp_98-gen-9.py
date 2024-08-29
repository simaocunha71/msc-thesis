
def multiply_num(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total / len(numbers)

print(multiply_num((8, 2, 3, -1, 7)))

"""
This function works by initializing a variable total to 1 (since multiplying any number by 1 gives the same number). 
Then it iterates through each number in the input tuple, multiplying the running total by that number. 
Finally, it divides the total by the length of the input tuple to get the average (which is the required result), 
and returns this value.
"""
<jupyter_output>
-67.2
<jupyter_text>
Question 2:
<jupyter_code>
