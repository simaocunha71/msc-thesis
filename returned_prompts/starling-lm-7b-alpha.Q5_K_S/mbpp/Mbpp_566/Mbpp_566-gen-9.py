"""
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
"""

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

assert sum_digits(345)==12

def test_sum_digits():
    assert sum_digits(345)==12
    assert sum_digits(123)==6
    assert sum_digits(40)==4
    assert sum_digits(0)==0
    print("All tests passed!")

test_sum_digits()

"""
def test_sum_digits():
    assert sum_digits(345)==12
    assert sum_digits(123)==6
    assert sum_digits(40)==4
    assert sum_digits(0)==0
    print("All tests passed!")
"""

"""
def test_sum_digits():
    assert sum_digits(345)==12
    assert sum_digits(123)==6
    assert sum_digits(40)==4
    assert sum_digits(0)==0
    print("All tests passed!")
"""

"""
def test_sum_digits():
    assert sum_digits(345)==12
    assert sum_digits(123)==6
    assert sum_digits(40)==4
    assert sum_digits(0)==0
    print("All tests passed!")
"""

"""
def test_sum_digits():
    assert sum_digits(345)==12
    assert sum_digits(123)==6
    assert sum_digits(40)==4
    assert sum_digits(0)==0
    print("All tests passed!")
"""

"""
def test_sum_digits