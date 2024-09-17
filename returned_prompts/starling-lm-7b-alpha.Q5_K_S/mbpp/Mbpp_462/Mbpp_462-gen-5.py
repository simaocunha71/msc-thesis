
def combinations_list(test_list, r):
    return [test_list[i:i+r] for i in range(len(test_list)+1-r)]


