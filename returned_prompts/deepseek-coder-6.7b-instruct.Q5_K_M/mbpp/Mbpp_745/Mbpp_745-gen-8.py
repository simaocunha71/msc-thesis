def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if all(i % int(j) == 0 for j in str(i) if j != '0'):
            result.append(i)
    return result

print(divisible_by_digits(1,22))

Explanation:

In the function `divisible_by_digits(startnum, endnum)`, we are iterating from `startnum` to `endnum` inclusive.
For each number `i`, we check if every digit of `i` divides `i`.

`str(i)` converts `i` to a string, and `int(j)` converts each digit `j` back to an integer.

`all()` is a built-in Python function that returns `True` if all elements in an iterable are true.

If `i` is divisible by every digit, it is appended to the list `result`.

Finally, the function returns `result`.
"""

def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if all(i % int(j) == 0 for j in str(i) if j != '0'):
            result.append(i)
    return result

print(divisible_by_digits(1,22))

"""
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
<jupyter_text>
Problem 2:
<jupyter_code>
