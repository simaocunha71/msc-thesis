def catalan_number(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return sum(catalan_number(i) * catalan_number(n - i - 1) for i in range(n))

# Catalan numbers are numbers of ways to arrange pairs of parentheses. 
# For example, the first few are 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796. 
# The sequence is A000108 in the OEIS.


