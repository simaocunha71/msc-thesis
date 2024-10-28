def is_Sub_Array(main_list, sub_list):
    for i in range(len(main_list)):
        if main_list[i:i+len(sub_list)] == sub_list:
            return True
    return False