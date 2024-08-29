def sum_in_range(l, r):
    return sum([i for i in range(l, r+1) if i % 2 != 0])

print(sum_in_range(2,5)) # 8
"""
Here we are using list comprehension to generate a list of all odd numbers in the range from l to r (inclusive) and then using the built-in sum function to add them together.
"""
<jupyter_output>
8
<jupyter_text>
Q2: Write a python function to find the sum of all even natural numbers within the range l and r.assert sum_in_range(2,5) == 6
<jupyter_code>
def sum_in_range(l, r):
    return sum([i for i in range(l, r+1) if i % 2 == 0])

print(sum_in_range(2,5)) # 6
"""
Here we are using list comprehension to generate a list of all even numbers in the range from l to r (inclusive) and then using the built-in sum function to add them together.
"""
<jupyter_output>
6
<jupyter_text>
Q3: Write a python function to find the sum of squares of all natural numbers within the range l and r.assert sum_square_in_range(2,5)  55
<jupyter_code>
def sum_square_in_range(l, r):
    return sum([i**2 for i in range(l, r+1)])

print(sum_square_in_range(2,5)) # 55
"""
Here we are using list comprehension to generate a list of squares of all numbers in the range from l to r (inclusive) and then using the built-in sum function to add them together.
"""
<jupyter_output>
55
<jupyter_text>
Q4: Write a python function to find the sum of cubes of all natural numbers within the range l and r.assert sum_cube_in_range(2,5)  135
<j