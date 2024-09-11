"""
def toggle_middle_bits(n):
    n = bin(n)[2:]
    n = n[:-1] + '0' + n[-1]
    return int(n, 2)

def test_toggle_middle_bits():
    assert toggle_middle_bits(9) == 15

test_toggle_middle_bits()
"""

def toggle_middle_bits(n):
    n = bin(n)[2:]
    n = n[:-1] + '0' + n[-1]
    return int(n, 2)

def test_toggle_middle_bits():
    assert toggle_middle_bits(9) == 15

test_toggle_middle_bits()


