def list_split(my_list, n):
    result = []
    for i in range(0, len(my_list), n):
        result.append(my_list[i:i+n])
    return result
