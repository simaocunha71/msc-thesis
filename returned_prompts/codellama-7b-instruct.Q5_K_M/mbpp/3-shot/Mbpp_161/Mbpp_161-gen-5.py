
def remove_elements(my_list, remove_list):
    result = []
    for num in my_list:
        if num not in remove_list:
            result.append(num)
    return result


