
def find_Max_Num(digits):
    def is_digit_valid(digit):
        return digit >= 0 and digit <= 9
    if not digits or not all(map(is_digit_valid, digits)):
        return -1

    digits.sort(reverse=True)
    result = 0
    for digit in digits:
        result = result * 10 + digit
    return result


