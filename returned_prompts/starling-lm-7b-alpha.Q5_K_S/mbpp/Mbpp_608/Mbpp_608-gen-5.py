def bell_Number(n):
    if (n == 0):
        return 1
    else:
        return (2*bell_Number(n-1) + (n-1)*bell_Number(n-2))

# assert bell_Number(2) == 2
# print(bell_Number(2))



"""
def bell_Number(n):
    if n == 0:
        return 1
    else:
        return 2 * bell_Number(n - 1) + (n - 1) * bell_Number(n - 2)

print(bell_Number(2))
"""

"""
def bell_Number(n):
    assert 0 <= n
    if n == 0:
        return 1
    else:
        return 2 * bell_Number(n - 1) + (n - 1) * bell_Number(n - 2)

def test_bell_number():
    assert bell_Number(2) == 2
    print(test_bell_number())
"""
"""
def bell_Number(n):
    assert (0 <= n)
    if (n == 0):
        return 1
    else:
        return (2*bell_Number(n-1) + (n-1)*bell_Number(n-2))

def test_bell_number():
    assert bell_Number(2) == 2
    print(test_bell_number())
"""
"""
def bell_Number(n):
    if (n == 0):
        return 1
    else:
        return (2*bell_Number(n-1) + (n-1)*bell_Number(n-2))

def test_bell_number():
    assert bell_Number(2) == 2
    print(test_bell_number())
"""
"""
def bell_Number(n):
    if n == 0:
        return 1
    else:
        return (2*bell_Number(n - 1) + (n - 1) * bell_Number(n - 2))

def test_bell_number():
    assert bell_Number(2