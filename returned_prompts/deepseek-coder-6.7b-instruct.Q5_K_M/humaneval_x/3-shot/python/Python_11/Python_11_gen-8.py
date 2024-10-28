    result = []

    for a_bit, b_bit in zip(a, b):
        result.append(str(int(a_bit) ^ int(b_bit)))

    return ''.join(result)

