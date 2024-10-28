    sum_ = array[0] + array[-1]
    if sum_ % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

