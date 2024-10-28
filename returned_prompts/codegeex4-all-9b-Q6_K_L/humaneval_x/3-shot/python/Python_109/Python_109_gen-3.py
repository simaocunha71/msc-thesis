    if len(arr) == 0:
        return True

    sorted_arr = sorted(arr)
    min_element = min(arr)
    min_index = arr.index(min_element)

    if min_index == 0:
        return True

    if min_element == sorted_arr[0]:
        return True

    return False

