def find_solution(a, b, n):
    for x in range(n):
        for y in range(n):
            if a * x + b * y == n:
                return (x, y)
    return None

print(find_solution(2, 3, 7))
<jupyter_output>
(2, 1)
<jupyter_text>
Problem 4:
<jupyter_code>
