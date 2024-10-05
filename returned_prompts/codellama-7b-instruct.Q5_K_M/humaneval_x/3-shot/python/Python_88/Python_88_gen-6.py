    array_sum = sum(array)
    sorted_array = array

    if array_sum % 2 == 0:
        sorted_array.sort(reverse=True)
    else:
        sorted_array.sort()

    return sorted_array


