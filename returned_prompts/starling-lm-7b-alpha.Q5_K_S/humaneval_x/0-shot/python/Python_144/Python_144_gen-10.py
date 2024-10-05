
def simplify(x, n):
    #convert to floats
    x = float(x)
    n = float(n)
    #find gcd
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    #find gcd
    gcd = gcd(x[0]*n[1], x[1]*n[0])
    #divide numerator and denominator by gcd
    x = (x[0]/gcd, x[1]/gcd)
    n = (n[0]/gcd, n[1]/gcd)
    #check if fraction is simplified
    if x == n:
        return True
    return False


# Alternative solution
# def simplify(x, n):
#     x_numerator, x_denominator = map(int, x.split('/'))
#     n_numerator, n_denominator = map(int, n.split('/'))

#     # calculate the greatest common divisor (gcd) of the two fractions
#     gcd = gcd(x_numerator, x_denominator) * gcd(n_numerator, n_denominator)

#     # calculate the simplified numerator and denominator
#     simplified_numerator = (x_numerator * n_denominator + x_denominator * n_numerator) // gcd
#     simplified_denominator = gcd

#     # check if the fraction is simplified
#     if simplified_numerator * simplified_denominator == x_numerator * n_denominator:
#         return True
#     return False

# This alternative solution uses the same logic as the previous one, but it uses the built-in `map` function to extract the numerator and denominator from the input strings. It also uses the built-in `gcd` function to calculate the greatest common divisor of two numbers.

```python
# Here are some test cases you can use to verify your implementation:

print(simplify("1/5", "5/1"))  # True
print(simplify("1