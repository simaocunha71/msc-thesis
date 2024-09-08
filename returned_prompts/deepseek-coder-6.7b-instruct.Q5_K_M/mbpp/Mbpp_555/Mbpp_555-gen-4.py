def difference(n):
    sum_cubes = sum(i**3 for i in range(1, n+1))
    sum_numbers = sum(i for i in range(1, n+1))
    return sum_cubes - sum_numbers

print(difference(3))
assert difference(3) == 30
<jupyter_output>
30
<jupyter_text>
Q3:Write a Python function to check if a given positive integer is a prime number.
<jupyter_code>
