    array_copy = array.copy()
    if sum(array[0], array[-1]) % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()
    return array_copy


