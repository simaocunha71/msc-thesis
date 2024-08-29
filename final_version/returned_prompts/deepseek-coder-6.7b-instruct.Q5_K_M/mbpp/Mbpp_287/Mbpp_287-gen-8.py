def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += (2*i)**2
    return sum

print(square_Sum(2))

# Output: 16
<jupyter_output>
16
<jupyter_text>
Q5
<jupyter_code>
"""
Write a python function takes in an integer n and returns the sum of squares