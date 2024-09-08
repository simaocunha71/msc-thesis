def angle_complex(z):
    return np.arctan2(np.imag(z), np.real(z))

print(math.isclose(angle_complex(0+1j), 1.5707963267948966, rel_tol=0.001))
"""

