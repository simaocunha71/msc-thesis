    array = array.copy() # we don't want to change the original array
    if len(array) < 2:
        return array

    if (array[0] + array[-1]) % 2 == 0: # if sum is even
        array.sort(reverse=True)
    else:
        array.sort()

    return array


