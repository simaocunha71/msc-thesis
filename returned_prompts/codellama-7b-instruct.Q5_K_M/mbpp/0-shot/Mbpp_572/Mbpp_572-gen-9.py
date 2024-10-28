def two_unique_nums(my_list):
    result = []
    for i in my_list:
        if i not in result:
            result.append(i)
    return result
