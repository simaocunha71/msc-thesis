"""
def check(num):
    if int(str(num)[::-1]) * 2 - 1 == num:
        return True
    else:
        return False

def test_check():
    assert check(70) == False
    print("All tests passed!")

test_check()
"""

def check(num):
    if num == int(str(num)[::-1]) * 2 - 1:
        return True
    else:
        return False

def test_check():
    assert check(70) == False
    print("All tests passed!")

test_check()









"""
"""

def check(num):
    num_str = str(num)
    num_str_reverse = num_str[::-1]
    if int(num_str_reverse) * 2 - 1 == num:
        return True
    else:
        return False

def test_check():
    assert check(70) == False
    print("All tests passed!")

test_check()
"""
"""

def check(num):
    num_str = str(num)
    num_str_reverse = num_str[::-1]
    if num == int(num_str_reverse) * 2 - 1:
        return True
    else:
        return False

def test_check():
    assert check(70) == False
    print("All tests passed!")

test_check()
"""

"""
"""
def check(num):
    if int(str(num)[::-1]) * 2 - 1 == num:
        return True
    else:
        return False

def test_check():
    assert check(70) == False
    print("All tests passed!")

test_check()
"""

"""
"""
def check(num):
    num_str = str(num)
    num_str_reverse = num_str[::-1]
    if num == int(num_str_reverse) * 2 - 1:
        return True
    else:
        return False

def