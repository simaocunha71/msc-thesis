
def get_equal(lst):
    for tup in lst:
        if len(tup) != len(lst[0]):
            return False
    return True

print(get_equal([(11, 22, 33), (44, 55, 66)]))

# 2.

