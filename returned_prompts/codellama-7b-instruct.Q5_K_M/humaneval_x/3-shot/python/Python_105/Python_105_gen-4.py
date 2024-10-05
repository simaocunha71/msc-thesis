    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]
    result = []

    for i in reversed_arr:
        if 1 <= i <= 9:
            result.append(names[i - 1])

    return result

