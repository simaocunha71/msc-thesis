"""
def left_insertion(sorted_list, value):
    left = 0
    right = len(sorted_list) - 1
    while left < right:
        if value < sorted_list[(left + right) // 2]:
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1
    return left

def test():
    assert left_insertion([1,2,4,5],6)==4
    assert left_insertion([1,2,3,4,5],3)==3
    assert left_insertion([1,2,3,4,5],4)==3
    assert left_insertion([1,2,3,4,5],5)==4
    assert left_insertion([1,2,3,4,5],6)==4
    print("All tests passed.")

test()
"""

def left_insertion(sorted_list, value):
    left = 0
    right = len(sorted_list) - 1
    while left < right:
        if value < sorted_list[(left + right) // 2]:
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1
    return left

def test():
    assert left_insertion([1,2,4,5],6)==4
    assert left_insertion([1,2,3,4,5],3)==3
    assert left_insertion([1,2,3,4,5],4)==3
    assert left_insertion([1,2,3,4,5],5)==4
    assert left_insertion([1,2,3,4,5],6)==4
    print("All tests passed.")

test()


In this code, the left_insertion function takes a sorted_list and a value as input, and it returns the left insertion point for the specified value in sorted order. The function uses a binary search algorithm to find the insertion point. The while loop continues until the left pointer is less than the