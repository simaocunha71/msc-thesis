def is_sublist(test_tup1, test_tup2):
    for i in range(len(test_tup1)-len(test_tup2)+1):
        if test_tup1[i:i+len(test_tup2)] == test_tup2:
            return True
    return False