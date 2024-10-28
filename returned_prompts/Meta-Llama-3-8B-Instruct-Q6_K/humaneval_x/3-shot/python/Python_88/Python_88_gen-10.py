    array_copy = array[:]  # make a copy of the array
    if sum(array[0], array[-1]) % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()
    return array_copy


