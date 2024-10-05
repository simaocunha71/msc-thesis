    result = ""
    for a_digit, b_digit in zip(a, b):
        if a_digit == '1' and b_digit == '1':
            result += '0'
        else:
            result += '1'
    return result


