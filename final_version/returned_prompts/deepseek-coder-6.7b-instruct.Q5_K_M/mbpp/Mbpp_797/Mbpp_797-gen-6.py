
def sum_in_range(l, r):
    odd_numbers = [num for num in range(l, r+1) if num % 2 != 0]
    return sum(odd_numbers)

print(sum_in_range(2,5)) # 8


"""
Explanation:
The function sum_in_range takes two arguments: l and r. It generates a list of all odd numbers in the range from l to r (inclusive). It does this by using a list comprehension with a condition: only include a number if it's odd (num % 2 != 0). It then returns the sum of these numbers using the built-in sum function.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Prime NumbersWrite a Python function that returns a list of all prime numbers within the range l and r.
<jupyter_code>
