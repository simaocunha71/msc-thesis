
def get_equal(lst):
    for i in lst:
        if len(i) != len(lst[0]):
            return False
    return True

print(get_equal([(11, 22, 33), (44, 55, 66)])) # True

"""
