    if not array:
        return array
    if len(array) == 1:
        return array
    return sorted(array, reverse=(array[0] + array[-1]) % 2)


