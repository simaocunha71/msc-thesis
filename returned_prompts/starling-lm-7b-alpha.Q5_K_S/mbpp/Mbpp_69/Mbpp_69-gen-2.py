"""
def is_sublist(list1,list2):
    if len(list1)<len(list2):
        return False
    for i in range(len(list2)):
        if list1[i]!=list2[i]:
            return False
    return True
"""

def is_sublist(list1,list2):
    if len(list1)<len(list2):
        return False
    for i in range(len(list2)):
        if list1[i]!=list2[i]:
            return False
    return True





"""
def is_sublist(list1,list2):
    if len(list1)<len(list2):
        return False
    for i in range(len(list2)):
        if list1[i]!=list2[i]:
            return False
    return True
"""




def test_is_sublist():
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[3,7,6])==True
    assert is_sublist([1,2,3,4],[2,3,4,5])==False
    print("All test cases pass")

test_is_sublist()

"""
def test_is_sublist():
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[3,7,6])==True
    assert is_sublist([1,2,3,4],[2,3,4,5])==False
    print("All test cases pass")

test_is_sublist()
"""

"""
def test_is_sublist():
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[3,7,6])==True
    assert is_sublist([1,2,3,4],[2,