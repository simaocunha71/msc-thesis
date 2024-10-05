    # Bisection method
    a = -1000.0
    b = 1000.0

    while True:
        c = (a + b) / 2
        if poly(xs, a) * poly(xs, c) <= 0:
            b = c
        else:
            a = c

        if abs(poly(xs, c)) < 1e-6:  # precision
            return c

# test the function
print(find_zero([-6, 11, -6, 1]))

