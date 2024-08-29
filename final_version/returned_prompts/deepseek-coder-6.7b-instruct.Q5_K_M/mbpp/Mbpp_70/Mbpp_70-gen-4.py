
def get_equal(lst):
    return all(len(x) == len(lst[0]) for x in lst)

print(get_equal([(11, 22, 33), (44, 55, 66)]))


