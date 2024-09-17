def closest_num(n: int) -> int:
    num = n - 1
    while num >= 0:
        if is_prime(num):
            return num
        num -= 1
    return None