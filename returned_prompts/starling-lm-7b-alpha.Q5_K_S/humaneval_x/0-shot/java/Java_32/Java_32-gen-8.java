        while (true) {
            double x = Math.random();
            if (poly(xs, x) == 0) {
                return x;
            }
        }
    }

    /**
    Compute a zero of a polynomial using Newton-Raphson method.
    Inputs:
    xs: coefficients of polynomial.
    x_init: initial guess of zero point.
    tol: tolerance for stopping criterion.
    max_iter: maximum number of iterations.
    >>> findZero(Arrays.asList(1, 2), 0)
    -0.5
    >>> findZero(Arrays.asList(-6, 11, -6, 1), 1)
    1.0
    >>> findZero(Arrays.asList(-6, 11, -6, 1), 0.5)
    1.0
    >>> findZero(Arrays.asList(1, 2), 2)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 0)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 1)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 2)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 3)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 4)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 5)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 6)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 7)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 8)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 9)
    -0.5
    >>> findZero(Arrays.asList(1, 2), 10)
    -0.5
    >>> findZero(