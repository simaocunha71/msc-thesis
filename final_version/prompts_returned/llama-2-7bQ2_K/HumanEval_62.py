

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    
    if len(xs) == 0:
        return []

    s = len(xs) - 1
    
    def deriv_one(p: int):
        if p == 0:
            return 0.0
        elif p == 2:
            return 3/4.0 + 1/2.0 * (s-1)/4.0 # -s / 8.0 + s/4.0
    def deriv_two(p: int):
        if p == 1:
            return 6.0 / (2.0 + s)
        elif p == 3:
            return 3 * (s-1)/2.0 - 5/8.0
    return map(deriv_two, range(-1, len(xs))) + map(deriv_one, range(-1, len(xs)-1))
        
    