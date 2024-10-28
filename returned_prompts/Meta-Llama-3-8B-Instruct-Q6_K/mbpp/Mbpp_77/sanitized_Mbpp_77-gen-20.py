def is_Diff(n):
    num = str(n)
    if len(num) % 2 == 0:
        return sum(int(digit) for digit in num[::2]) - sum(int(digit) for digit in num[1::2]) == 0
    else:
        return sum(int(digit) for digit in num[::2]) - sum(int(digit) for digit in num[1::2]) % 11 == 0