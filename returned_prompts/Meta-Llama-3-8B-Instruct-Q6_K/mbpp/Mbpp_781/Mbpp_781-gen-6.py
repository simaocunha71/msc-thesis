def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count % 2 == 0
assert count_divisors(10)
print(count_divisors(10))  # True
print(count_divisors(9))  # False
print(count_divisors(12))  # True
print(count_divisors(15))  # False
print(count_divisors(16))  # True
print(count_divisors(20))  # False
print(count_divisors(21))  # True
print(count_divisors(24))  # False
print(count_divisors(25))  # True
print(count_divisors(30))  # False
print(count_divisors(36))  # True
print(count_divisors(40))  # False
print(count_divisors(48))  # True
print(count_divisors(50))  # False
print(count_divisors(54))  # True
print(count_divisors(60))  # False
print(count_divisors(64))  # True
print(count_divisors(72))  # False
print(count_divisors(75))  # True
print(count_divisors(80))  # False
print(count_divisors(81))  # True
print(count_divisors(84))  # False
print(count_divisors(90))  # True
print(count_divisors(96))  # False
print(count_divisors(100))  # True
print(count_divisors(120))  # False
print(count_divisors(126))  # True
print(count_divisors(128))  # False
print(count_divisors(144))  # True
print(count_divisors(150))  # False
print(count_divisors(160))  # True
print(count_divisors(162))  # False
print(count_divisors(180))  # True
print(count_divisors(192))  # False
print(count_divisors(200))  # True
print(count_divisors(216))  # False
print(count_divisors(225))  # True
print(count_divisors(240))  # False
print(count_divisors(243))  # True
print(count_divisors(250))  # False
print(count_divisors(256))  # True
print(count_divisors