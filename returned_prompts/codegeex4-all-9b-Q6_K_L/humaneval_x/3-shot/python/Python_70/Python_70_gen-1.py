    sorted_lst = sorted(lst)
    result = []
    while sorted_lst:
        result.append(sorted_lst.pop(0))
        if sorted_lst:
            result.append(sorted_lst.pop(-1))
    return result

