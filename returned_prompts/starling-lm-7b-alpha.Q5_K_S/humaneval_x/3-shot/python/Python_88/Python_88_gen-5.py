    if (array[0] + array[len(array)-1]) % 2 == 0:
        array.sort(reverse=True)
    else:
        array.sort()
    return array


