"""
def number_ctr(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1
    return count

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()
"""

def number_ctr(s):
    return len([c for c in s if c.isdigit()])

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()

def number_ctr(s):
    return len(list(filter(str.isdigit, s)))

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()

def number_ctr(s):
    return len(filter(str.isdigit, s))

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()

def number_ctr(s):
    return len(list(map(str.isdigit, s)))

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()

def number_ctr(s):
    return s.count(str.digit)

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()

def number_ctr(s):
    return sum(1 for c in s if c.isdigit())

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()

def number_ctr(s):
    return len(set(c for c in s if c.isdigit()))

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()

def number_ctr(s):
    return sum(len(c) for c in s if c.isdigit())

def test_number