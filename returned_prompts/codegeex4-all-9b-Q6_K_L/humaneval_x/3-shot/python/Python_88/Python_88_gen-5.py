    if len(array) == 0:
        return []
    if len(array) == 1:
        return array

    sum = array[0] + array[-1]

    if sum % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)