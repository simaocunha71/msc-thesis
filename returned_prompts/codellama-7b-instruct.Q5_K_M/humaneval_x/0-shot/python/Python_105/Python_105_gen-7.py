
def by_length(arr):
    arr_sort = sorted(arr)
    arr_reverse = arr_sort[::-1]
    arr_name = []

    for i in arr_reverse:
        if 1 <= i <= 9:
            arr_name.append(str(i))
        else:
            continue

    arr_name = [i.capitalize() for i in arr_name]
    arr_name = [i + " " + str(i) for i in arr_name]

    return arr_name


