    if not array:
        return array

    first = array[0]
    last = array[-1]

    if (first + last) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)


