def bell_Number(n):
    bells = [0, 1]
    for i in range(2, n + 1):
        bells.append(sum(bells[i - 1::]))
    return bells[n]


"""
def bell_number(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return sum([bell_number(i-1) for i in range(n+1)])

def bell_number(n):
    bells = [0, 1]
    for i in range(2, n + 1):
        bells.append(sum(bells[i - 1::]))
    return bells[n]
"""

def test_bell_Number():
    assert bell_Number(2) == 2

test_bell_Number()




"""
def bell_number(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return sum([bell_number(i-1) for i in range(n+1)])
"""


def test_bell_Number():
    assert bell_Number(2) == 2

test_bell_Number()




"""
def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return sum(bell_Number(i-1) for i in range(n+1))
"""

def test_bell_Number():
    assert bell_Number(2) == 2

test_bell_Number()




"""
def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return sum(bell_Number(i-1) for i in range(n+1))
"""

def test_bell_Number():
    assert bell_Number(2) == 2

test_bell_Number()




"""
def bell