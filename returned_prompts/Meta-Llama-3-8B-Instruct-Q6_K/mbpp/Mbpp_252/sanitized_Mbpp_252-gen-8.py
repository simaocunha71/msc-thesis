def convert(complex_num):
    import cmath
    polar_coords = cmath.polar(complex_num)
    return polar_coords[0], polar_coords[1]  # return magnitude and phase separately