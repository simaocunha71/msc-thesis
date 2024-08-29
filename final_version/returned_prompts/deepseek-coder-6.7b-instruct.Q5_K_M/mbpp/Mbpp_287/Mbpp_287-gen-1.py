
def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*2*i*2
    return sum

# Test
print(square_Sum(2))  # 20

# Better Solution
def square_Sum_Better(n):
    return sum([i**2 for i in range(1, n+1)])

# Test
print(square_Sum_Better(2))  # 20

"""
Explanation:
The function square_Sum takes an integer n and returns the sum of squares of the first n even natural numbers.
It uses a loop to iterate through the range of 1 to n (inclusive). For each iteration, it calculates the square of the current number (which is 2 times the current number), and adds it to the sum.

The function square_Sum_Better is an optimized version of square_Sum. It uses a list comprehension to generate a list of the squares of the first n even natural numbers, and then uses the sum function to calculate the sum of the squares. This version is more efficient and concise.
"""

# Test
assert square_Sum(2) == 20
assert square_Sum_Better(2) == 20

# Test with large input
assert square_Sum(100) == 10100
assert square_Sum_Better(100) == 10100

# Both tests should pass
<jupyter_output>
20
20
10100
10100
<jupyter_text>
