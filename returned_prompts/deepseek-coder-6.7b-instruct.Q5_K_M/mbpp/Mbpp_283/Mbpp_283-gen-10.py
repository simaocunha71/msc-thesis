
def validate(n):
    digits = [int(x) for x in str(n)]
    return all(digit <= count for digit, count in enumerate(digits))


