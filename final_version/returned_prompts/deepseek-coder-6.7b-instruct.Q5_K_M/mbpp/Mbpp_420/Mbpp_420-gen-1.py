
def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * 2 * i * 2
    return sum

# Test
print(cube_Sum(2))  # 72

# Code Explanation:
# A for loop is used to calculate the cube sum of first n even natural numbers.
# The formula used here is i * 2 (to get the even number) * i (to cube it) and this is added to the running sum.
# Finally, the sum is returned.
<jupyter_output>
72
<jupyter_text>
Question 2
<jupyter_code>
