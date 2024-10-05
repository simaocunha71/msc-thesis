    result = ''
    for idx, (a_bit, b_bit) in enumerate(zip(a, b)):
        if a_bit == b_bit:
            result += '0'
        else:
            result += '1'

    return result


