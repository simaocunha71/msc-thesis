
def square_Sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**2
    return sum

print(square_Sum(2))
<jupyter_output>
10
<jupyter_text>
2. Python program to find the sum of squares of first n natural numbers
<jupyter_code>
