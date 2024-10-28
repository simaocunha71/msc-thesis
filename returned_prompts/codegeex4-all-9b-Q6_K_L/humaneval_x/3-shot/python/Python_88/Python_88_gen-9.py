    if len(array) < 2:
        return array

    first_value = array[0]
    last_value = array[-1]
    sum_values = first_value + last_value

    if sum_values % 2 == 0:
        sorted_array = sorted(array, reverse=True)
    else:
        sorted_array = sorted(array)

    return sorted_array

