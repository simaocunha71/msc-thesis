    sum_first_last = array[0] + array[-1]

    if sum_first_last % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

