"""
def extract_index_list(l1, l2, l3):
    result = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            result.append(l1[i])
    return result

# Unit Tests

def test_extract_index_list():
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    print("All tests passed.")

test_extract_index_list()
"""

from collections import Counter

def extract_index_list(l1, l2, l3):
    return [i for i in l1 if i in l2 and i in l3]

# Unit Tests

def test_extract_index_list():
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    print("All tests passed.")

test_extract_index_list()



def extract_index_list(l1, l2, l3):
    return list(set(l1) & set(l2) & set(l3))

# Unit Tests

def test_extract_index_list():
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    print("All tests passed.")

test_extract_index_list()


def extract_index_list(l1, l2