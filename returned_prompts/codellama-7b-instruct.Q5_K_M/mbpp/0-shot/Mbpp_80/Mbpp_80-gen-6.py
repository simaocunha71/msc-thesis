
# The nth tetrahedral number is the number of dots in a tetrahedron with n dots.
# The number of dots is (n * (n + 1)) / 2
# https://en.wikipedia.org/wiki/Tetrahedral_number
def tetrahedral_number(n):
    return int((n * (n + 1)) / 2)
