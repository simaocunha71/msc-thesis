

def largest_divisor(n: int) -> int:
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1


print(largest_divisor(15))

# Test cases
print(largest_divisor(1))  # 1
print(largest_divisor(2))  # 1
print(largest_divisor(3))  # 1
print(largest_divisor(4))  # 2
print(largest_divisor(15))  # 5
print(largest_divisor(21))  # 7
print(largest_divisor(24))  # 8
print(largest_divisor(100))  # 50
print(largest_divisor(999999))  # 99999