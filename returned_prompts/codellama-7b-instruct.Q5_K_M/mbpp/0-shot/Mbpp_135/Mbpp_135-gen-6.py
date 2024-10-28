"""
Hexagonal numbers are constructed by summing the numbers of the triangular numbers that are
adjacent to them. The triangular numbers are the numbers of the triangular numbers
(1, 3, 6, 10, 15, etc.). For example, the first hexagonal number is 1, because the first
triangular number 1+2+3 = 6. The second hexagonal number is 7, because the second triangular
number 1+3+5 = 9.
"""

def hexagonal_num(n):
    if n == 1:
        return 1
    else:
        return triangular_num(n) - triangular_num(n-1)

def triangular_num(n):
    return n*(n+1)/2

# test
# assert hexagonal_num(10) == 190
# assert hexagonal_num(100) == 1533776805
# assert hexagonal_num(1000) == 14316557661
