def cube_Sum(n):
    total = 0
    even_num = 2
    for _ in range(n):
        total += even_num ** 3
        even_num += 2
    return total

print(cube_Sum(2))

# Output: 72
<jupyter_output>
72
<jupyter_text>
Question 2
<jupyter_code>
