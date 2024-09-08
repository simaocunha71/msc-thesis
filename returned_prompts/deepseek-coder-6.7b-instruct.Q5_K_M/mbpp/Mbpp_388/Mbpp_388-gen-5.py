def highest_Power_of_2(n):
    i = 0
    while (1 << i) <= n:
        i += 1
    return 1 << (i - 1)

print(highest_Power_of_2(10))

"""
Explanation:
This function works by using bitwise shift operator to calculate 2 to the power of i.
It starts by initializing i to 0 and then increments it in each iteration until 2 to the power of i is greater than n.
At that point, it returns 2 to the power of (i - 1) which is the highest power of 2 that is less than or equal to n.
"""

# Test Cases
assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(15) == 8
assert highest_Power_of_2(16) == 16
assert highest_Power_of_2(20) == 16
assert highest_Power_of_2(32) == 32
assert highest_Power_of_2(1024) == 1024
assert highest_Power_of_2(1023) == 512
assert highest_Power_of_2(0) == 0
assert highest_Power_of_2(1) == 1
<jupyter_output>
8
<jupyter_text>
Problem 6: Find the missing number in a given list of integers.
<jupyter_code>
