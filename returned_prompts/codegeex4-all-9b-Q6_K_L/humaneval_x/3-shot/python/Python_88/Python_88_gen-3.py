    sum_of_first_and_last = array[0] + array[-1]
    sorted_array = sorted(array)

    if sum_of_first_and_last % 2 == 0:
        return sorted_array[::-1]
    else:
        return sorted_array

