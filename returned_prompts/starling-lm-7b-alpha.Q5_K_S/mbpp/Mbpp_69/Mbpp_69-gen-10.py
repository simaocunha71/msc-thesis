"""
def is_sublist(li,sub_li):
    if len(sub_li) > len(li):
        return False
    for i in range(len(li)-len(sub_li)+1):
        if li[i:i+len(sub_li)] == sub_li:
            return True
    return False
"""

def is_sublist(li,sub_li):
    if len(sub_li) > len(li):
        return False
    for i in range(len(li)-len(sub_li)+1):
        if li[i:i+len(sub_li)] == sub_li:
            return True
    return False


def test_is_sublist():
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[2,3,5])==True
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[2,4])==True
    assert is_sublist([2,4,3,5,7],[2,4,3])==True
    assert is_sublist([2,4,3,5,7],[2,4,3,5])==True
    assert is_sublist([2,4,3,5,7],[2,4,3,5,7])==True
    assert is_sublist([2,4,3,5,7],[2,4,3,5,8])==False
    assert is_sublist([],[])==True
    assert is_sublist([1],[1])==True

test_is_sublist()
print('All tests passed.')


"""
Test Cases:

1. is_sublist([2,4,3,5,7],[3,7]) -- False
2. is_sublist([2,4,3,5,7],[2,3,5]) -- True
3. is_sublist([2,4,3,5