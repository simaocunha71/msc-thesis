
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    return x if is_prime(n) else y

# Test cases
print(x_or_y(7, 34, 12))  # should return 34
print(x_or_y(15, 8, 5))  # should return 5
print(x_or_y(1, 100, 200))  # should return 200
print(x_or_y(2, 300, 400))  # should return 300
print(x_or_y(0, 500, 600))  # should return 600

# Check if the function is working as expected
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5
assert x_or_y(1, 100, 200) == 200
assert x_or_y(2, 300, 400) == 300
assert x_or_y(0, 500, 600) == 600
<jupyter_output>
34
5
200
300
600
<jupyter_text>
