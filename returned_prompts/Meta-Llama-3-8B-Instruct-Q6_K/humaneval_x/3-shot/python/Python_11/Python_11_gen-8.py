    result = ''
    for i in range(max(len(a), len(b))):
        bit_a = a[-1 - i] if i < len(a) else '0'
        bit_b = b[-1 - i] if i < len(b) else '0'
        result = str(int(bit_a) ^ int(bit_b)) + result
    return result


