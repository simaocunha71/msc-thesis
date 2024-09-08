
def multiply_num(num_list):
    total = 1
    for num in num_list:
        total *= num
    return total / len(num_list)

print(multiply_num((8, 2, 3, -1, 7)))

# 1. Create a variable total and set it to 1.
# 2. Iterate over each number in the given list.
# 3. Multiply the current total by the number.
# 4. After iterating over all the numbers, divide the total by the length of the list.
# 5. Return the result.

# 6. The final result should be the product of all the numbers in the list, divided by the length of the list.
# 7. Use the math.isclose function to compare the result with the expected output, with a relative tolerance of 0.001.
# 8. If the result is close enough to the expected output, the function should return True. Otherwise, it should return False.
<jupyter_output>
-67.2
<jupyter_text>
Q2:Write a Python program that prompts the user for a list of integers, then prints a list of the squares of those numbers. Use a list comprehension to do this in one line.
<jupyter_code>
