def is_Diff(n):
    n = str(n)
    even_sum = sum(int(digit) for i, digit in enumerate(n) if i % 2 == 0)
    odd_sum = sum(int(digit) for i, digit in enumerate(n) if i % 2 != 0)
    return even_sum - odd_sum % 11 == 0