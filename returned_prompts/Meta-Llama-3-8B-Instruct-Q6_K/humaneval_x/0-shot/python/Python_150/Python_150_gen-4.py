    def x_or_y(n, x, y):
        if is_prime(n):
            return x
        else:
            return y

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

# Testing the function
print(x_or_y(7, 34, 12))  # Expected output: 34
print(x_or_y(15, 8, 5))   # Expected output: 5
print(x_or_y(11, 34, 12))  # Expected output: 34
print(x_or_y(20, 8, 5))   # Expected output: 5
print(x_or_y(2, 34, 12))   # Expected output: 34
print(x_or_y(3, 34, 12))   # Expected output: 34
print(x_or_y(4, 34, 12))   # Expected output: 5
print(x_or_y(9, 34, 12))   # Expected output: 5
print(x_or_y(6, 34, 12))   # Expected output: 5
print(x_or_y(8, 34, 12))   # Expected output: 5
print(x_or_y(10, 34, 12))  # Expected output: 5
print(x_or_y(14, 34, 12))  # Expected output: 5
print(x_or_y(16, 34, 12))  # Expected output: 5
print(x_or_y(18, 34, 12))  # Expected output: 5
print(x_or_y(19, 34, 12))  # Expected output: 34
print(x_or_y(21, 34, 12))  # Expected output: 5
print(x_or_y(22, 34, 12))  # Expected output: 5
print(x_or_y(23, 34, 12))  # Expected output: 34
print(x_or_y(25, 34, 12))  # Expected output: 5
print(x_or_y(26, 34, 12))  # Expected output: 5
print(x_or_y(27