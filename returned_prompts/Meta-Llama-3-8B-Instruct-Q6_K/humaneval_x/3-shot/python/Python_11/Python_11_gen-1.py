    result = ''
    for a_bit, b_bit in zip(a, b):
        if a_bit == '1' and b_bit == '1':
            result += '0'
        elif a_bit == '0' and b_bit == '0':
            result += '0'
        else:
            result += '1'

    return result


