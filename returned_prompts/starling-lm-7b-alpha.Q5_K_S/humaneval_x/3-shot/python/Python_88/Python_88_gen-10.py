    array_copy = array.copy()
    array_copy.sort()
    if (array_copy[0] + array_copy[-1]) % 2 == 0:
        array_copy.reverse()
    return array_copy


