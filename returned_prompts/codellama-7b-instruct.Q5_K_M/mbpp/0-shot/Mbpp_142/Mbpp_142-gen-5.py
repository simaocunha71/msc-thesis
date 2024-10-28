"""
def count_samepair(lst1, lst2, lst3):
    assert len(lst1) == len(lst2) == len(lst3)
    return sum(i == j and k == l for i, j, k, l in zip(lst1, lst2, lst3, lst3))
"""
