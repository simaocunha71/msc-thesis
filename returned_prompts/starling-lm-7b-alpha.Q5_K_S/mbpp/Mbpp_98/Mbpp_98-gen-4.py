"""
To solve the problem, we can follow these steps:

1. Create a function called multiply_num that takes a list of numbers as an argument.
2. Initialize a variable called result to 1. This variable will store the product of all the numbers in the list.
3. Iterate through each number in the list using a for loop. For each number, multiply it with the current value of result and update the value of result.
4. After the loop, divide the result by the length of the list using the len() function and store the result in a variable called final_result.
5. Finally, return the final_result from the multiply_num function.
6. Use the assert statement to check if the result of multiplying the numbers in the list (8, 2, 3, -1, 7) is approximately equal to -67.2 with a relative tolerance of 0.001.
"""

import math

def multiply_num(num_list):
    result = 1
    for num in num_list:
        result *= num
    final_result = result / len(num_list)
    return final_result

assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)

# Here's the code for the multiply_num function:

"""
def multiply_num(num_list):
    result = 1
    for num in num_list:
        result *= num
    final_result = result / len(num_list)
    return final_result
"""

"""
To use the function, you can pass a list of numbers as an argument to the multiply_num function. For example, in the assert statement above, we passed the list (8, 2, 3, -1, 7) to the function and checked if the result is approximately equal to -67.2 with a relative tolerance of 0.001.
"""

"""
The assert statement is used to check if a condition is true. In this case, we are using it to check if the result of multiplying the numbers in the list is approximately equal to -67.2 with a