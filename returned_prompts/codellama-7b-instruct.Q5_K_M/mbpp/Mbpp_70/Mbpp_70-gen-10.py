
def get_equal(my_list):
    return all(len(tup) == len(my_list[0]) for tup in my_list)


