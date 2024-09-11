"""
def min_k(tup_list, k):
    tup_list = sorted(tup_list, key=lambda x: x[1])
    return tup_list[:k]

def test_min_k():
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    print("All Test Cases Passed!")

test_min_k()
"""

def min_k(tup_list, k):
    tup_list = sorted(tup_list, key=lambda x: x[1])
    return tup_list[:k]

def test_min_k():
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    print("All Test Cases Passed!")

test_min_k()






"""
def min_k(tup_list, k):
    tup_list = sorted(tup_list, key=lambda x: x[1])
    return tup_list[:k]

def test_min_k():
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    print("All Test Cases Passed!")

test_min_k()
"""

"""
def min_k(tup_list, k):
    tup_list = sorted(tup_list, key=lambda x: x[1])
    return tup_list[:k]

def test_min_k():
    assert min_k([('Manjeet', 10), ('Akshat', 