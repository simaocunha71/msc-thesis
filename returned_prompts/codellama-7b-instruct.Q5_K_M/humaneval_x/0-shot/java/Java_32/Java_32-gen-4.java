        if (xs.size() == 0) {
            return 0;
        }

        if (xs.size() == 1) {
            return 0;
        }

        if (xs.size() % 2 == 1) {
            return 0;
        }

        double b = xs.get(xs.size() - 2);
        double c = xs.get(xs.size() - 1);
        double delta = b * b - 4 * c;
        if (delta < 0) {
            return 0;
        }
        if (delta == 0) {
            return -b / 2;
        }
        double x1 = (-b + Math.sqrt(delta)) / 2;
        double x2 = (-b - Math.sqrt(delta)) / 2;
        if (x1 < x2) {
            return x1;
        }
        return x2;
    }

    /**
    xs are coefficients of a polynomial.
    findZeros finds all zero points of the polynomial.
    findZeros returns list of zero points.
    >>> findZeros(Arrays.asList(1, 2)) // f(x) = 1 + 2x
    [0.0]
    >>> findZeros(Arrays.asList(-6, 11, -6, 1)) // (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [-0.5, 1.0]
     */
    public List<Double> findZeros(List<Double> xs) {
        List<Double> result = new ArrayList<>();
        double x0 = findZero(xs);
        result.add(x0);
        double x1 = x0;
        double x2 = x0;
        while (Math.abs(x1 - x2) > 1e-10) {
            xs.set(xs.size() - 1, xs.get(xs.size() - 1) + 0.00001);
            x2 = find