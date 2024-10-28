    double a = xs[0];
    double b = xs[1];
    double c = xs[2];
    double d = xs[3];
    return -b / (2 * c);
}  // Note that this function assumes that xs has at least 3 elements (i.e., at least a quadratic term) and that the largest non-zero coefficient is the leading coefficient of the polynomial. If these assumptions are not valid, the function may not work correctly.