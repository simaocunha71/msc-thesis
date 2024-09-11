def substract_elements(t1, t2):
    return tuple(t1[i] - t2[i] for i in range(len(t1)))

def test_substract_elements():
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)

test_substract_elements()










"""
def substract_elements(t1, t2):
    return tuple(t1[i] - t2[i] for i in range(len(t1)))

def test_substract_elements():
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)

test_substract_elements()
"""

"""
def subtract_tuples(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] - t2[i])
    return tuple(result)

def test_subtract_tuples():
    assert subtract_tuples((10, 4, 5), (2, 5, 18)) == (8, -1, -13)

test_subtract_tuples()
"""
"""
def subtract_tuples(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] - t2[i])
    return result

def test_subtract_tuples():
    assert subtract_tuples((10, 4, 5), (2, 5, 18)) == [8, -1, -13]

test_subtract_tuples()
"""
"""
def subtract_tuples(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] - t2[i])
    return result

def test_subtract_tuples():
    t1 = (