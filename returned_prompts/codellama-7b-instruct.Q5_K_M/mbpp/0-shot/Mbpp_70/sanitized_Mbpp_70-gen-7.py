def get_equal(my_list):
    if len(set(len(x) for x in my_list)) == 1:
        return True
    else:
        return False