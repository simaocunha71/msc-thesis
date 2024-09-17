def consecutive_duplicates(test_list):
    for i in range(len(test_list)-1):
        if test_list[i] == test_list[i+1]:
            del test_list[i+1]
    return test_list