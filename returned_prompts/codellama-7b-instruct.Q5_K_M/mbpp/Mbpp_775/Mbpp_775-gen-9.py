def odd_position(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0 and i % 2 != 0:
            return False
    return True
