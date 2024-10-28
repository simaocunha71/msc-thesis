    # Find_zero find x such that poly(x) = 0
    # find_zero returns only one zero point, even if there are many.
    # Moreover, find_zero only takes list xs having even number of coefficients
    # and largest non zero coefficient as it guarantees
    # a solution.
    # The reason is that if the degree of the polynomial is odd, then one of the
    # coefficients is zero and the polynomial is not defined for zero value of x.
    # If the degree of the polynomial is even, then there is always one root
    # at x=0.
    # https://en.wikipedia.org/wiki/Real_root_test
    # The test is based on the fact that if a polynomial has all its coefficients positive,
    # then it must have a real root.
    # If the polynomial does not have all its coefficients positive, then it must have a
    # real root if the degree is even, and it may or may not have a real root if the degree
    # is odd.
    # Note that the test is sufficient but not necessary.

    # The test is based on the fact that if a polynomial has all its coefficients positive,
    # then it must have a real root.
    # If the polynomial does not have all its coefficients positive, then it must have a
    # real root if the degree is even, and it may or may not have a real root if the degree
    # is odd.
    # Note that the test is sufficient but not necessary.

    # Since the coefficients are all positive, then the polynomial must have a real root.
    # The real root must be between the two roots of the quadratic equation
    # ax^2 + b = 0, where a = xs[0], b = -xs[1].
    # Then, the zero of the polynomial is the average of the two roots of the quadratic equation.
    # The two roots of the quadratic equation are the solutions of the equation ax^2 + b = 0.
    # The two roots are:
    # x = (-b ± sqrt(b^2 - 4ac)/(2a)
    # In Python, it can be calculated as follows:
    a = xs[0]
    b = -xs[