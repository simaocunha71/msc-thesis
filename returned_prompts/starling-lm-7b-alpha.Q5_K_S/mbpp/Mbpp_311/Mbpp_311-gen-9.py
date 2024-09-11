"""
def set_left_most_unset_bit(n):
    return n | (n + 1)
"""

def set_left_most_unset_bit(n):
    return n | (n + 1)

# testing
assert set_left_most_unset_bit(10) == 14

# testing
assert set_left_most_unset_bit(1) == 3

# testing
assert set_left_most_unset_bit(0) == 1

# testing
assert set_left_most_unset_bit(2) == 5

# testing
assert set_left_most_unset_bit(15) == 30

# testing
assert set_left_most_unset_bit(30) == 62

# testing
assert set_left_most_unset_bit(62) == 124

# testing
assert set_left_most_unset_bit(124) == 248

# testing
assert set_left_most_unset_bit(248) == 496

# testing
assert set_left_most_unset_bit(496) == 992

# testing
assert set_left_most_unset_bit(992) == 1984

# testing
assert set_left_most_unset_bit(1984) == 3968

# testing
assert set_left_most_unset_bit(3968) == 7936

# testing
assert set_left_most_unset_bit(7936) == 15872

# testing
assert set_left_most_unset_bit(15872) == 31744

# testing
assert set_left_most_unset_bit(31744) == 63488

# testing
assert set_left_most_unset_bit(63488) == 126976

# testing
assert set_left_most_