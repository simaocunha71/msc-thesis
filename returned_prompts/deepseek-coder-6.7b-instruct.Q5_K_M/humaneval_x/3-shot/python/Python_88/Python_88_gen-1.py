    array_copy = array[:]
    if (array_copy[0] + array_copy[-1]) % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()
    return array_copy


