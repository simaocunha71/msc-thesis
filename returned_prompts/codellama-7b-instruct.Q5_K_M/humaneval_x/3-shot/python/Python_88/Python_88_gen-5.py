    if not array:
        return []

    even_odd_sum = sum(array) % 2

    if even_odd_sum == 0:
        array.sort(reverse=True)
    else:
        array.sort()

    return array


