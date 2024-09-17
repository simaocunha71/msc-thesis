def validate(n):
    str_n = str(n)
    return all(int(str_n.count(digit)) <= int(digit) for digit in str_n)