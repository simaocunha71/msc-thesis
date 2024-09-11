"""
def count_X(tup, ele):
    count = 0
    for i in tup:
        if i == ele:
            count += 1
    return count

"""

def count_X(tup, ele):
    return tup.count(ele)


assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0

"""

