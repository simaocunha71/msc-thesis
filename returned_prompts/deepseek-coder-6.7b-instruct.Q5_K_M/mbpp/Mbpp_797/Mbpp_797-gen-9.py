def sum_in_range(l, r):
    return sum(x for x in range(l, r+1) if x % 2 != 0)

print(sum_in_range(2, 5))

# 2nd method
def sum_in_range(l, r):
    return sum(x for x in range(l, r+1) if x % 2)

print(sum_in_range(2, 5))

# 3rd method
def sum_in_range(l, r):
    return sum(x for x in range(l, r+1) if x & 1)

print(sum_in_range(2, 5))

# 4th method
def sum_in_range(l, r):
    return sum(x for x in range(l, r+1, 2))

print(sum_in_range(2, 5))
<jupyter_output>
8
8
8
8
<jupyter_text>
Q2:
<jupyter_code>
"""
Write a python function to find the sum of squares of all natural numbers within the range l and r.
assert sum_sq_in_range(2,5) == 55
"""

def sum_sq_in_range(l, r):
    return sum(x*x for x in range(l, r+1))

print(sum_sq_in_range(2, 5))
<jupyter_output>
55
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a python function to find the sum of squares of all odd natural numbers within the range l and r.
assert sum_sq_odd_in_range(2,5) == 16
"""

def sum_sq_odd_in_range(l, r):
    return sum(x*x for x in range(l, r+1) if x % 2 != 0)

print(sum_sq_odd_in_range(2, 5))
<jupyter_output>
16
<j