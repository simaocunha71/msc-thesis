    array_copy = array.copy()
    first_last_sum = array_copy[0] + array_copy[-1]
    if first_last_sum % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()
    return array_copy


