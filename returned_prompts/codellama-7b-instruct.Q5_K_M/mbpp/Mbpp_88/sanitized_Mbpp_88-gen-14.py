def freq_count(my_list):
    result = {}
    for element in my_list:
        if element not in result:
            result[element] = 0
        result[element] += 1
    return result