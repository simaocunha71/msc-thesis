def is_Sub_Array(big_list, small_list):
    for i in range(len(big_list)):
        if big_list[i:i+len(small_list)] == small_list:
            return True
    return False