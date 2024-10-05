
def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    if x == 1:
        return True
    if n == 1:
        return False
    return int(n ** (1.0 / math.log(n, x))) == n

# 9

