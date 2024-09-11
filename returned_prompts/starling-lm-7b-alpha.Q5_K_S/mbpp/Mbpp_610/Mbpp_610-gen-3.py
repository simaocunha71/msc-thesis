"""
def remove_kth_element(l,k):
    return l[:k] + l[k+1:]

def test_remove_kth_element():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    print("All tests passed!")

test_remove_kth_element()
"""

# Using List comprehension
"""
def remove_kth_element(l,k):
    return [i for j,i in enumerate(l) if j != k]

def test_remove_kth_element():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    print("All tests passed!")

test_remove_kth_element()
"""

# Using slicing
"""
def remove_kth_element(l,k):
    return l[:k]+l[k+1:]

def test_remove_kth_element():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    print("All tests passed!")

test_remove_kth_element()
"""

# Using del keyword
"""
def remove_kth_element(l,k):
    del l[k]
    return l

def test_remove_kth_element():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    print("All tests passed!")

test_remove_kth_element()
"""

# Using pop() method
"""
def remove_kth_element(l,k):
    l.pop(k)
    return l

def test