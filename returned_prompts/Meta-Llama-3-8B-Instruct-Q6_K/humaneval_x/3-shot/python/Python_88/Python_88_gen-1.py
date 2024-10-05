    def sum_first_last(arr):
        return arr[0] + arr[-1]

    arr = array.copy()
    if sum_first_last(arr) % 2 == 0:
        arr.sort(reverse=True)
    else:
        arr.sort()

    return arr
    # or return sorted(array, reverse=bool(sum_first_last(array) % 2))  # Python3.7+
    # or return sorted(array, reverse=(sum_first_last(array) % 2 != 0))  # Python3.7+


