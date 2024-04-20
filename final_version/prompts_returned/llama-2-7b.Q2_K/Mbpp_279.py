"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""

def get_n_digits(x):
    return np.ceil(np.log10(x)) + 9

def is_n_powers_of_10(n, m=5):
    """assert n > 0
    assert len(str(n)) <= 3
    """
    if not (len(str(n)) <= 3):
        print('assert: n < 2**5')
        sys.exit(-1)
    if not (np.isclose(np.log10(n), np.power(10, get_n_digits(x)))):
        print('assert: n < pow(10, get_n_digits(n))')
        sys.exit(-1)
    return True

def is_triangular():
    """assert (x >= 0 and x <= 1) & (y >= 0 and y <= 1)"""
    assert np.all(np.logspace(0, 2, 7).astype('i8')[None, :].flatten() >= 0) & \
           np.all(np.array(range(7)).tolist()[None, :] >= 0) & \
           is_n_powers_of_10(-2 ** 7, m=5) & \
            (is_n_powers_of_10(*x[:-6]) for x in np.logspace(0, -4, 6)) & \
            is_triangular(*np.array([-3, -2, -1]).tolist()[None, :])
        sys.exit(-1)
    return True

def decagonal():
    """assert (x >= 0 and x <= 10)"""
    assert np.all(np.logspace(0, 1, 7).astype('i8')[None, :].flatten() >= 0) & \
           np.all(np.array([-3, -2, -1]).tolist()[None, :] >= 0) & \
           is_triangular(*np.logspace(0, -4, 6))
    return True