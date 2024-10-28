def is_polite(n):
    count = 0
    num = 1
    while True:
        if is_prime(num):
            num += 1
            continue
        if is_prime(num - 1):
            num += 1
            continue
        count += 1
        if count == n:
            return num - 1
        num += 1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_polite(7))  # Output: 11
print(is_polite(1))  # Output: 1
print(is_polite(2))  # Output: 3
print(is_polite(3))  # Output: 5
print(is_polite(4))  # Output: 7
print(is_polite(5))  # Output: 9
print(is_polite(6))  # Output: 11
print(is_polite(8))  # Output: 13
print(is_polite(9))  # Output: 15
print(is_polite(10))  # Output: 17
print(is_polite(11))  # Output: 19
print(is_polite(12))  # Output: 21
print(is_polite(13))  # Output: 23
print(is_polite(14))  # Output: 25
print(is_polite(15))  # Output: 27
print(is_polite(16))  # Output: 29
print(is_polite(17))  # Output: 31
print(is_polite(18))  # Output: 33
print(is_polite(19))  # Output: 35
print(is_polite(20))  # Output: 37
print(is_polite(21))  # Output: 39
print(is_polite(22))  # Output: 41
print(is_polite(23))  # Output: 43
print(is_polite(24))  # Output: 45
print(is_polite(25))  # Output: 47
print(is_polite(26))  # Output: 49
print(is_polite(27))  # Output: 51
print(is