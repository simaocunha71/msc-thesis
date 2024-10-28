
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

print(x_or_y(7, 34, 12))  # should return 34
print(x_or_y(15, 8, 5))  # should return 5

#Test cases
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5
assert x_or_y(2, 100, 200) == 100
assert x_or_y(3, 300, 400) == 300
assert x_or_y(4, 400, 500) == 400
assert x_or_y(5, 500, 600) == 500
assert x_or_y(6, 600, 700) == 600
assert x_or_y(8, 800, 900) == 800
assert x_or_y(9, 900, 1000) == 900
assert x_or_y(10, 1000, 1100) == 1000
print("All test cases passed")
<jupyter_output>
34
5
All test cases passed
<jupyter_text>
