    if len(xs) % 2 == 1:
        raise ValueError('xs should have even number of elements')

    if xs[0] == 0:
        raise ValueError('largest coefficient should be non zero')

    # find first non zero coefficient
    largest_idx = 0
    for idx, coeff in enumerate(xs):
        if coeff != 0:
            largest_idx = idx
            break

    # find x0 that makes poly(x0) = 0
    x0 = 0
    for i in range(1, largest_idx + 1):
        x0 -= poly(xs[largest_idx - i:], x0) / poly([1] * i, 1)

    return x0


