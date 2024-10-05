    if not array:
        return array
    if len(array) == 1:
        return array

    sum_of_first_and_last = array[0] + array[-1]

    return sorted(array, reverse=bool(sum_of_first_and_last % 2))


