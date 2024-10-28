
def x_or_y(n, x, y):
    if n == 2 or n == 3:
        return x
    if n % 2 == 0 or n == 1:
        return y
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return y
    return x

print(x_or_y(7, 34, 12)) # 34
print(x_or_y(15, 8, 5)) # 5
print(x_or_y(2, 3, 1)) # 3
print(x_or_y(4, 5, 6)) # 6
print(x_or_y(11, 12, 13)) # 12
print(x_or_y(14, 15, 16)) # 16
<jupyter_output>
34
5
3
6
12
16
<jupyter_text>
