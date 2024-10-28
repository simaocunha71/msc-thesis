    sorted_list = sorted(lst)
    result = []
    i = 0

    while i < len(sorted_list):
        result.append(sorted_list[i])
        i += 1

        if i < len(sorted_list):
            result.append(sorted_list[-i - 1])
            i += 1

    return result

