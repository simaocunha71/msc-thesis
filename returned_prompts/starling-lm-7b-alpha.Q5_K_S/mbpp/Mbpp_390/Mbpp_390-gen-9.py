"""
def add_string(lst,format_str):
    lst = [format_str.format(i) for i in range(len(lst))]
    return lst

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    print("All tests passed")

test_add_string()
"""

# Another solution
def add_string(lst,format_str):
    return [format_str.format(i) for i in range(len(lst))]

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    print("All tests passed")

test_add_string()

# One-liner solution
def add_string(lst,format_str):
    return [format_str.format(i) for i in range(len(lst))]

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    print("All tests passed")

test_add_string()
"""

# Another solution
def add_string(lst,format_str):
    return [format_str.format(i) for i in range(len(lst))]

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    print("All tests passed")

test_add_string()
"""

# Another solution
def add_string(lst,format_str):
    return [format_str.format(i) for i in range(len(lst))]

def test_add_string():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    print("All tests