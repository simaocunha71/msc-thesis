
def hexagonal_num(n):
    return n * (2 * n - 1)

# Tests
assert hexagonal_num(10) == 190
assert hexagonal_num(26) == 556
assert hexagonal_num(5) == 35
assert hexagonal_num(1) == 1

