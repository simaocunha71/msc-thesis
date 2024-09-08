def cube_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**3
    return sum

print(cube_Sum(2))
assert cube_Sum(2) == 72
<jupyter_output>
72
<jupyter_text>
Q2:
<jupyter_code>
