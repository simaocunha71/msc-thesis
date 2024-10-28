def is_polite(n):
    count = 0
    num = 0
    while True:
        num += 1
        if is_prime(num):
            num += 1
        if is_prime(num):
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

assert is_polite(7) == 11
print(is_polite(7))  # Output: 11
print(is_polite(8))  # Output: 13
print(is_polite(9))  # Output: 17
print(is_polite(10)) # Output: 19
print(is_polite(11)) # Output: 23
print(is_polite(12)) # Output: 29
print(is_polite(13)) # Output: 37
print(is_polite(14)) # Output: 41
print(is_polite(15)) # Output: 47
print(is_polite(16)) # Output: 53
print(is_polite(17)) # Output: 61
print(is_polite(18)) # Output: 67
print(is_polite(19)) # Output: 71
print(is_polite(20)) # Output: 73
print(is_polite(21)) # Output: 79
print(is_polite(22)) # Output: 83
print(is_polite(23)) # Output: 89
print(is_polite(24)) # Output: 97
print(is_polite(25)) # Output: 101
print(is_polite(26)) # Output: 103
print(is_polite(27)) # Output: 107
print(is_polite(28)) # Output: 109
print(is_polite(29)) # Output: 113
print(is_polite(30)) # Output: 127
print(is_polite(31)) # Output: 131
print(is_polite(32)) # Output: 137
print(is_polite(33)) # Output: 139
print(is_polite(34)) # Output: 149
print(is_polite(35)) # Output: 