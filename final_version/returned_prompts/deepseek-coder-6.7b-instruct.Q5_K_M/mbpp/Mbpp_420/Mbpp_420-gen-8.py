def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        num = 2 * i
        sum += num ** 3
    return sum

print(cube_Sum(2))

# Test Case
assert cube_Sum(2) == 72

# Output: 72
<jupyter_output>
72
<jupyter_text>
**Question 10**
<jupyter_code>
