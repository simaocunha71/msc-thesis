
def get_equal(tup_list):
    return all(map(lambda x: len(x) == len(tup_list[0]), tup_list))


