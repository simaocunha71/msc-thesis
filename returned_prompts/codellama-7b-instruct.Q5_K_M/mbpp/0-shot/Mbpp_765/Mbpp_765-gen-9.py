def is_polite(n):
    digits = list(str(n))
    for i in range(len(digits)):
        if digits[i] == '0':
            return False
        if int(digits[i]) == i + 1:
            continue
        else:
            return False
    return True

def nth_polite(n):
    if n == 1:
        return 0
    if is_polite(n-1):
        return n-1
    else:
        return nth_polite(n-1)

print(nth_polite(30))  # 25
print(nth_polite(31))  # 26
print(nth_polite(32))  # 27
print(nth_polite(33))  # 28
print(nth_polite(34))  # 29
print(nth_polite(35))  # 30
print(nth_polite(36))  # 31
print(nth_polite(37))  # 32
print(nth_polite(38))  # 33
print(nth_polite(39))  # 34
print(nth_polite(40))  # 35
print(nth_polite(41))  # 36
print(nth_polite(42))  # 37
print(nth_polite(43))  # 38
print(nth_polite(44))  # 39
print(nth_polite(45))  # 40
print(nth_polite(46))  # 41
print(nth_polite(47))  # 42
print(nth_polite(48))  # 43
print(nth_polite(49))  # 44
print(nth_polite(50))  # 45
print(nth_polite(51))  # 46
print(nth_polite(52))  # 47
print(nth_polite(