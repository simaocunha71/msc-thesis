
def multiply(a, b):
    a_unit = int(str(abs(a))[-1])
    b_unit = int(str(abs(b))[-1])
    return a_unit * b_unit

print(multiply(148, 412))  # 16
print(multiply(19, 28))  # 72
print(multiply(2020, 1851))  # 0
print(multiply(14, -15))  # 20

# Solution:
# This solution works by getting the unit digit of each number by converting the absolute value of the number to a string, taking the last character, and converting it back to an integer. It then multiplies these unit digits together to get the result.

# The function abs is used to get the absolute value of the numbers, because the unit digit of a negative number is the same as the unit digit of its positive counterpart. 

# This solution has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input. It has a space complexity of O(1) because it uses a fixed amount of space to store the unit digits.

# The solution is correct because it correctly calculates the product of the unit digits of the two input integers.
<jupyter_output>
16
72
0
20
<jupyter_text>
Problem 5
<jupyter_code>
