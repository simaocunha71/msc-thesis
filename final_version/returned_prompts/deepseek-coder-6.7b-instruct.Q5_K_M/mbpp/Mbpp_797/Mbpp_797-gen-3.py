def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)

print(sum_in_range(2, 5))

# Explanation:
# The function sum_in_range takes two parameters l and r. 
# It uses a generator comprehension to generate all odd numbers in the range of l and r. 
# It then uses the built-in sum function to sum up all these numbers and returns the result.
<jupyter_output>
8
<jupyter_text>
Q3: Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
<jupyter_code>
