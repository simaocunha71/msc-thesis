"""
def consecutive_duplicates(list_):
    result = []
    for i in range(len(list_) - 1):
        if list_[i] == list_[i + 1]:
            continue
        else:
            result.append(list_[i])
    result.append(list_[-1])
    return result
"""
def consecutive_duplicates(list_):
    return [x for i, x in enumerate(list_, 1) if list_[i - 1] != x]


def test_consecutive_duplicates():
    assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    assert consecutive_duplicates([1, 2, 3, 3, 4, 5, 5, 6, 6]) == [1, 2, 3, 4, 5, 6]
    assert consecutive_duplicates([1, 2, 3, 3, 4, 5, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert consecutive_duplicates([1, 2, 3, 3, 4, 5, 5, 6, 6]) == [1, 2, 3, 4, 5, 6]
    assert consecutive_duplicates([1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 4, 4]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    assert consecutive_duplicates([1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8,