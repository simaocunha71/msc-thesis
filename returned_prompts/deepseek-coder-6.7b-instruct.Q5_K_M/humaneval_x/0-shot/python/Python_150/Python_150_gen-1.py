
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return x if is_prime(n) else y

# Testing
print(x_or_y(7, 34, 12))  # 34
print(x_or_y(15, 8, 5))  # 5
print(x_or_y(2, 8, 5))  # 8
print(x_or_y(1, 8, 5))  # 5
print(x_or_y(4, 10, 20))  # 20
print(x_or_y(3, 10, 20))  # 10
<jupyter_output>
34
5
8
5
20
10
<jupyter_text>
