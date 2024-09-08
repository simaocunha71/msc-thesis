def angle_complex(z):
    if z.real > 0:
        return np.arctan(z.imag/z.real)
    elif z.real < 0 and z.imag >= 0:
        return np.arctan(z.imag/z.real) + np.pi
    elif z.real < 0 and z.imag < 0:
        return np.arctan(z.imag/z.real) - np.pi
    elif z.real == 0 and z.imag > 0:
        return np.pi/2
    elif z.real == 0 and z.imag < 0:
        return -np.pi/2
    else:
        return 0