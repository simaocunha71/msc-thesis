    result = []
    for a_elem, b_elem in zip(a, b):
        if a_elem == b_elem:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


