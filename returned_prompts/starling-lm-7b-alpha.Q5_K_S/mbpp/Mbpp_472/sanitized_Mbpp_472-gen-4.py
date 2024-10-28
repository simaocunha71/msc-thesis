def check_Consecutive(num_list):
    # check if the list is empty or contains only one element
    if len(num_list) == 0 or len(num_list) == 1:
        return True
    # sort the list
    num_list.sort()
    # compare each element with its successor
    for i in range(len(num_list) - 1):
        if num_list[i] + 1 != num_list[i + 1]:
            return False
    return True