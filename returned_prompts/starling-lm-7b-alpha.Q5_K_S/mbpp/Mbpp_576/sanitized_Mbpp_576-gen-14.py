def is_Sub_Array(test_arr1, test_arr2):
    for i in range(len(test_arr1)):
        if (test_arr2 == test_arr1[i:]):
            return True
    return False