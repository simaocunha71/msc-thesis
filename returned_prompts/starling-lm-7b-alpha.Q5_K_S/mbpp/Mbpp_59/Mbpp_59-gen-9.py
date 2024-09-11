def is_octagonal(n):
    return n == 0 or is_square(n) or is_hexagonal(n)

def is_square(n):
    return n == 0 or n % 4 == 0

def is_hexagonal(n):
    return n == 0 or n % 6 == 0

def octagonal(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * n**2 - 3*n + 4


# Test
assert(is_octagonal(0) == True)
assert(is_octagonal(1) == True)
assert(is_octagonal(2) == True)
assert(is_octagonal(3) == True)
assert(is_octagonal(4) == True)
assert(is_octagonal(5) == True)
assert(is_octagonal(6) == True)
assert(is_octagonal(7) == True)
assert(is_octagonal(8) == True)
assert(is_octagonal(9) == True)
assert(is_octagonal(10) == True)
assert(is_octagonal(11) == True)
assert(is_octagonal(12) == True)
assert(is_octagonal(13) == True)
assert(is_octagonal(14) == True)
assert(is_octagonal(15) == True)
assert(is_octagonal(16) == True)
assert(is_octagonal(17) == True)
assert(is_octagonal(18) == True)
assert(is_octagonal(19) == True)
assert(is_octagonal(20) == True)
assert(is_octagonal(21) == True)
assert(is_octagonal(22) == True)
assert(is_octagonal(23) == True)
assert(is_octagonal(24) == True)
assert(is_octagonal(25) == True)
assert(is_octagonal(26) == True)
assert(is_