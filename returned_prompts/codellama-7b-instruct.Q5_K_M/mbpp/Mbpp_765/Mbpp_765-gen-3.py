def is_polite(n):
    if n < 10:
        return n
    else:
        num = str(n)
        if len(num) == 3:
            if int(num[0]) <= int(num[2]) and int(num[1]) <= int(num[2]):
                return int(num[0]) + int(num[2])
            else:
                return n + 1
        else:
            if int(num[0]) <= int(num[1]) and int(num[1]) <= int(num[2]):
                return int(num[0]) + int(num[2])
            else:
                return n + 1
"""
assert is_polite(1) == 1
assert is_polite(11) == 12
assert is_polite(22) == 23
assert is_polite(111) == 112
assert is_polite(123) == 124
assert is_polite(1111) == 1112
assert is_polite(11111) == 11112
assert is_polite(111111) == 111112
assert is_polite(123456) == 123457
assert is_polite(1111111) == 1111112
assert is_polite(11111111) == 11111112
assert is_polite(111111111) == 111111112
assert is_polite(1111111111) == 1111111112
assert is_polite(11111111111) == 1111111112
assert is_polite(111111111111) == 1111111112
assert is_polite(1111111111111