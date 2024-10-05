    original_sum = array[0] + array[-1]
    if original_sum % 2 == 0:
        array = sorted(array, reverse=True)
    else:
        array = sorted(array)
    return array


