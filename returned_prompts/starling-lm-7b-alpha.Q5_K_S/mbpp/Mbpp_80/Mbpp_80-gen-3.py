def tetrahedral_number(n):
    return (n * (n + 1) * (n + 2)) // 6

# Tests
assert tetrahedral_number(5) == 35





"""
The nth tetrahedral number is the number of dots needed to make a tetrahedron out of dots in a grid.
For example, the 5th tetrahedral number is 35, which corresponds to the following grid:

  . . . . . . . .
  . . . . . . . .
  . . . . . . . .
    . . . . . . .
    . . . . . . .
      . . . . . .

It can be calculated as (n * (n + 1) * (n + 2)) // 6
"""






"""
The nth tetrahedral number is the number of dots needed to make a tetrahedron out of dots in a grid.
For example, the 5th tetrahedral number is 35, which corresponds to the following grid:

  . . . . . . . .
  . . . . . . . .
  . . . . . . . .
    . . . . . . .
    . . . . . . .
      . . . . . .

It can be calculated as (n * (n + 1) * (n + 2)) // 6
"""





def tetrahedral_number(n):
    return (n * (n + 1) * (n + 2)) // 6

# Tests
assert tetrahedral_number(5) == 35





"""
A tetrahedron is a pyramid with a triangular base. In a grid, it can be created by taking a 3×3 block of dots and removing the central four dots. The number of dots in the tetrahedron is called the tetrahedral number.

For example, the 5th tetrahedral number is 35, which corresponds to the following grid:

  . . .