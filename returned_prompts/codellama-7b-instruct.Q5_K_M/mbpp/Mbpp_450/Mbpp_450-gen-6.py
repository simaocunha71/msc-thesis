
def extract_string(my_list,size):
    result = []
    for i in range(0, len(my_list), size):
        result.append(my_list[i])
    return result


