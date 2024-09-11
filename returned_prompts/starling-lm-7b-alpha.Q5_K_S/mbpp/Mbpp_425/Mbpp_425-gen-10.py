"""
def count_element_in_list(arr, elem):
    c = 0
    for sublist in arr:
        if elem in sublist:
            c += 1
    return c
"""

def count_element_in_list(arr, elem):
    c = 0
    for sublist in arr:
        if elem in sublist:
            c += 1
    return c


def test_count_element_in_list():
    assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
    print("All tests passed.")


test_count_element_in_list()

"""
"""

