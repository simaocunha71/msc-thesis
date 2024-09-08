def sumofFactors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    even_factors = [i for i in factors if i % 2 == 0]
    return sum(even_factors)

print(sumofFactors(18))  # 26

"""
In the above function, I first find all factors of the input number. Then, I use a list comprehension to select only the even factors. Finally, I return the sum of these even factors.
"""

"""
Test Cases:
assert sumofFactors(18) == 26
assert sumofFactors(24) == 42
assert sumofFactors(12) == 28
assert sumofFactors(30) == 72
assert sumofFactors(2) == 2
"""
<jupyter_output>
26
<jupyter_text>
Q3:Write a Python function to find the sum of all elements in a list using recursion.
<jupyter_code>
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

# Test cases
print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([5, 10, 15, 20, 25]))  # 75
print(sum_list([-1, -2, -3, -4, -5]))  # -15
<jupyter_output>
15
75
-15
<jupyter_text>
Q4:Write a Python function that accepts a string and returns a string where every word is reversed.
<jupyter_code>
def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Test cases