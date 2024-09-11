"""
def add_string(L,format):
    new_L = []
    for i in L:
        new_L.append(format.format(i))
    return new_L

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

test_add_string()
"""

# This solution is incorrect:
# The function add_string does not return a list of strings
def add_string(L,format):
    new_L = []
    for i in L:
        new_L.append(format.format(i))
    return new_L

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

test_add_string()

# Correct Solution:
def add_string(L,format):
    return [format.format(i) for i in L]

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

test_add_string()

# Using map function:
def add_string(L,format):
    return map(format.format, L)

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

test_add_string()

# Using list comprehension and map function:
def add_string(L,format):
    return map(format.format, (i for i in L))

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

test_add_string()

# Using join function:
def add_string(L,format):
    return format.join(map(format