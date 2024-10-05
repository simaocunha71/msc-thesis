def x_or_y(n, x, y):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True
    return x if is_prime(n) else y

print(x_or_y(7, 34, 12)) # 34
print(x_or_y(15, 8, 5)) # 5