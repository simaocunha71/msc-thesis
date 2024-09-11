def extract_index_list(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            l.append(l1[i])
    return l


print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))






"""
def extract_index_list(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            l.append(l1[i])
    return l

def test_extract_index_list():
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    print("All tests passed!")

test_extract_index_list()
"""





"""
def extract_index_list(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            l.append(l1[i])
    return l

def test_extract_index_list():
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    print("All tests passed!")

test_extract_index