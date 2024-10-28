def get_equal(tup_list):
    for i in range(len(tup_list)):
        if len(tup_list[i]) != len(tup_list[0]):
            return False
    return True