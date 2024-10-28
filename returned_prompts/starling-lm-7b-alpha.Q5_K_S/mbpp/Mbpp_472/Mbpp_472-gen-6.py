
def check_Consecutive(test_list):
    test_list.sort()
    for i in range(len(test_list)-1):
        if test_list[i+1] - test_list[i] != 1:
            return False
    return True


