def check_Consecutive(my_list):
    if len(my_list) <= 1:
        return False
    for i in range(len(my_list) - 1):
        if my_list[i+1] != my_list[i] + 1:
            return False
    return True
