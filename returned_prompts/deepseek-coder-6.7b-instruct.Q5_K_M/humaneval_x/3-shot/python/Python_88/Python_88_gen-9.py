    if not array:
        return array

    array = array[:]
    if (array[0] + array[-1]) % 2 == 0:
        array.sort(reverse=True)
    else:
        array.sort()

    return array


