    if sum(array[0], array[-1]) % 2 == 0:
        array = array[::-1]
    array.sort()
    return array


