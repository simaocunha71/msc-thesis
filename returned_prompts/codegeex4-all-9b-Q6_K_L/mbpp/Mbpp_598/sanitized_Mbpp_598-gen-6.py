def armstrong_number(num):
    digits = list(map(int, str(num)))
    n = len(digits)
    return num == sum(digit ** n for digit in digits)