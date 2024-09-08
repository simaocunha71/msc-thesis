
def odd_Equivalent(s, r):
    n = len(s)
    s = s + s
    odd = sum(x == '1' for x in s[:n]) % 2
    res = odd
    for i in range(n, r + n):
        if s[i] == '1':
            odd += 1
        if s[i - n] == '1':
            odd -= 1
        res += odd % 2
    return res

assert odd_Equivalent("011001", 6) == 3

Explanation:

In this problem, we first convert the string to binary. We then create a binary string by appending the original string to itself. The binary string is rotated in such a way that the binary string is divided into 'r' parts. We then calculate the count of numbers with odd values when the binary string is rotated 'r' times.

In the function odd_Equivalent(s, r), first we calculate the count of '1's in the first 'n' bits of the binary string. If the count is odd, then it means that the binary number is odd when read from left to right. We store this count in the variable 'odd'. 

We then start rotating the binary string. For each new bit in the string, if it is '1', we increase the 'odd' count by 1. If the new bit is '0', we keep the 'odd' count as it is. 

We also check if the old bit in the string is '1'. If it is '1', we decrease the 'odd' count by 1. If the old bit is '0', we keep the 'odd' count as it is. 

We then check if the 'odd' count is odd. If it is odd, we add 1 to the 'res' count. Otherwise, we keep 'res' as it is. 

Finally, we return the 'res' count. This count represents the number of numbers with an odd value when rotating the binary string the given number of times.
"""

# -------------------------
# Solution 2
# -------------------------
"""
