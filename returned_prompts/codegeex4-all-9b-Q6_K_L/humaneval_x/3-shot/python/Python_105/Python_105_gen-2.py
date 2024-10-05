    def number_to_name(num):
        names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return names[num - 1]

    filtered_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    result = [number_to_name(x) for x in reversed_arr]

    return result

