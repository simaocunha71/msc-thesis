

def sum_to_n(n: int):
    return sum(range(1, n + 1))


print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))




"""
This function uses the built-in Python function 'sum' to sum numbers in a range from 1 to n (inclusive). The 'range' function generates a sequence of numbers from 1 to n (inclusive). The '+1' in the range function is needed because the 'range' function doesn't include the end value in the sequence.
"""

#Test cases
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1

print("All test cases pass")
<jupyter_output>
465
5050
15
55
1
All test cases pass
<jupyter_text>
2. Write a Python function that checks if a given string is a palindrome (reads the same backwards as forwards).
<jupyter_code>
