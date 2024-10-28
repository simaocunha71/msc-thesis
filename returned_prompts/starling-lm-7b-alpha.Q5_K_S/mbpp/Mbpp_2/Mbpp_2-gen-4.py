"""
def similar_elements(list_a, list_b):
    return list(set(list_a) & set(list_b))

def test_similar_elements():
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))

if __name__ == "__main__":
    test_similar_elements()
"""

def similar_elements(list_a, list_b):
    return list(set(list_a) & set(list_b))

def test_similar_elements():
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))

if __name__ == "__main__":
    test_similar_elements()



def similar_elements(list_a, list_b):
    return list(set(list(a)) & set(list(b)))

def test_similar_elements():
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))

if __name__ == "__main__":
    test_similar_elements()



def similar_elements(list_a, list_b):
    return list(set(list(list_a)) & set(list(list_b)))

def test_similar_elements():
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))

if __name__ == "__main__":
    test_similar_elements()



def similar_elements(list_a, list_b):
    return list(set(list(list_a)) & set(list(list_b)))

def test_similar_elements():
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10