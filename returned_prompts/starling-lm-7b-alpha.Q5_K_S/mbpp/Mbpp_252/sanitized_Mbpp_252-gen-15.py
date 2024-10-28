import cmath
def convert(num_complex):
    mod = cmath.polar(num_complex)
    return (mod.real, mod.imag)