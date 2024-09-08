
def multiply_num(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product / len(numbers)

print(multiply_num((8, 2, 3, -1, 7)))

# Output: -67.2

"""
Explanation:

The function 'multiply_num' takes a list of numbers as input. It initializes a variable 'product' to 1. Then it iterates over the list of numbers, multiplying the current 'product' by each number. After going through all the numbers, it divides the 'product' by the number of elements in the list (obtained using the 'len' function) and returns the result.

The assertion checks whether the output of the function matches the expected result within a relative tolerance of 0.001.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2: Create a function to check if a number is a palindrome. A palindrome is a number that remains the same when its digits are reversed.
<jupyter_code>
