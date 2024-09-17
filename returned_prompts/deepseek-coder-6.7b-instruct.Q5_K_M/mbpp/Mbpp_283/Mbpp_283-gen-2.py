
def validate(n):
    num_str = str(n)
    return all(int(num_str.count(digit)) <= int(digit) for digit in num_str)


