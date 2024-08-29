def square_Sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**2
    return sum

assert square_Sum(2) == 10
"""
Explanation:
The first 2 odd numbers are 1 and 3, their squares are 1 and 9 respectively. Their sum is 10.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
