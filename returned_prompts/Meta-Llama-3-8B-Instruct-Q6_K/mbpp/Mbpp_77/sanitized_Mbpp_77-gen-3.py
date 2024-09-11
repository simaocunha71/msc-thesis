def is_Diff(n):
    return (sum(int(digit) for digit in str(n)) % 11) != 0