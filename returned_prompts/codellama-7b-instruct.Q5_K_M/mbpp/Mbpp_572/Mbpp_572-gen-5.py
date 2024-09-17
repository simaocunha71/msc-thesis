
def two_unique_nums(my_list):
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


