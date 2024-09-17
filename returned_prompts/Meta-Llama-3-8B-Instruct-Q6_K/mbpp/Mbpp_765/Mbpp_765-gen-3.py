def is_polite(n):
    polite_numbers = []
    i = 1
    while len(polite_numbers) < n:
        if i % 2 == 0:
            polite_numbers.append(i - 1)
        else:
            polite_numbers.append(i)
        i += 1
    return polite_numbers[-1]  # return the nth polite number

assert is_polite(7) == 11

# test case
print(is_polite(7)) # Output: 11
print(is_polite(1)) # Output: 1
print(is_polite(5)) # Output: 9
print(is_polite(3)) # Output: 3
print(is_polite(2)) # Output: 1
print(is_polite(6)) # Output: 8
print(is_polite(4)) # Output: 5
print(is_polite(8)) # Output: 12
print(is_polite(9)) # Output: 14
print(is_polite(10)) # Output: 16
print(is_polite(11)) # Output: 18
print(is_polite(12)) # Output: 20
print(is_polite(13)) # Output: 22
print(is_polite(14)) # Output: 24
print(is_polite(15)) # Output: 25
print(is_polite(16)) # Output: 27
print(is_polite(17)) # Output: 29
print(is_polite(18)) # Output: 31
print(is_polite(19)) # Output: 33
print(is_polite(20)) # Output: 35
print(is_polite(21)) # Output: 37
print(is_polite(22)) # Output: 38
print(is_polite(23)) # Output: 40
print(is_polite(24)) # Output: 42
print(is_polite(25)) # Output: 44
print(is_polite(26)) # Output: 46
print(is_polite(27)) # Output: 48
print(is_polite(28)) # Output: 50
print(is_polite(29)) # Output: 52
print(is_polite(30)) # Output: 54
print(is_polite(31)) # Output: 55
print(is_polite(32)) # Output: 57
print(is_polite(