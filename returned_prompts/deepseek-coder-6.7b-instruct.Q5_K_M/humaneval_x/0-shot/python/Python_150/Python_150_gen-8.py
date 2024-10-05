
def x_or_y(n, x, y):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

print(x_or_y(7, 34, 12))  # 34
print(x_or_y(15, 8, 5))  # 5
print(x_or_y(2, 10, 20))  # 10
print(x_or_y(3, 100, 200))  # 100
print(x_or_y(4, 1000, 2000))  # 2000
<jupyter_output>
34
5
10
100
2000
<jupyter_text>
Question 5:
<jupyter_code>
