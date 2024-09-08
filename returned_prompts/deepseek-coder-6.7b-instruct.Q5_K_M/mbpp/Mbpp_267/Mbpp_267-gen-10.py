def square_Sum(n):
    sum = 0
    for i in range(n):
        sum += (2*i + 1) ** 2
    return sum

print(square_Sum(2)) # 10

# Alternative solution using mathematical formula
def square_Sum_formula(n):
    return n * (n + 1) * (2 * n + 1) // 2

print(square_Sum_formula(2)) # 10
<jupyter_output>
10
10
<jupyter_text>
Question 3
<jupyter_code>
