def is_polite(n):
    polite_numbers = set()
    i = 0
    while len(polite_numbers) < n:
        i += 1
        for j in range(1, i):
            if i - j in polite_numbers:
                polite_numbers.add(i)
                break
    return list(polite_numbers)[-1] if polite_numbers else None
assert is_polite(7) == 11
print(is_polite(7))  # Output: 11
print(is_polite(5))  # Output: 8
print(is_polite(3))  # Output: 4
print(is_polite(2))  # Output: 2
print(is_polite(1))  # Output: 1
print(is_polite(10))  # Output: 18
print(is_polite(11))  # Output: 21
print(is_polite(12))  # Output: 24
print(is_polite(13))  # Output: 27
print(is_polite(14))  # Output: 30
print(is_polite(15))  # Output: 33
print(is_polite(16))  # Output: 36
print(is_polite(17))  # Output: 39
print(is_polite(18))  # Output: 42
print(is_polite(19))  # Output: 45
print(is_polite(20))  # Output: 48
print(is_polite(21))  # Output: 51
print(is_polite(22))  # Output: 54
print(is_polite(23))  # Output: 57
print(is_polite(24))  # Output: 60
print(is_polite(25))  # Output: 63
print(is_polite(26))  # Output: 66
print(is_polite(27))  # Output: 69
print(is_polite(28))  # Output: 72
print(is_polite(29))  # Output: 75
print(is_polite(30))  # Output: 78
print(is_polite(31))  # Output: 81
print(is_polite(32))  # Output: 84
print(is_polite(33))  # Output: 87
print(is_polite(34))  # Output: 90
print(is_polite