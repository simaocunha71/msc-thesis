def convert(complex_num):
    if isinstance(complex_num, complex):
        r = abs(complex_num)
        theta = cmath.phase(complex_num)
        return (r, theta)
    else:
        raise TypeError("Input must be a complex number")