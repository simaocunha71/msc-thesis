def check(n):
    rev = int(str(n)[::-1])
    twice_rev = 2 * rev
    return twice_rev - 1 == n

print(check(70))

# Output: False

# Explanation:
# The reverse of 70 is 07. Twice that is 14. Subtracting 1 from that gives 13, which is not equal to 70. Therefore, the condition is not met and the function returns False.
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
