def x_or_y(n, x, y):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return x if is_prime(n) else y

print(x_or_y(7, 34, 12))  # 34
print(x_or_y(15, 8, 5))  # 5