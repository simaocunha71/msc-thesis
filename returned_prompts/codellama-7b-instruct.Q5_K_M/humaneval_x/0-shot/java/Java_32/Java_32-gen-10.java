        if (xs.size() == 0) {
            throw new IllegalArgumentException("empty list");
        }
        if (xs.size() % 2 == 1) {
            throw new IllegalArgumentException("odd number of coefficients");
        }
        if (xs.get(xs.size() - 1) == 0) {
            throw new IllegalArgumentException("zero value of largest coefficient");
        }
        for (int i = 1; i < xs.size(); i += 2) {
            if (xs.get(i) == 0) {
                continue;
            }
            if (xs.get(i) < 0) {
                return -findZero(xs.subList(0, i) + xs.subList(i + 1, xs.size()));
            }
            return findZero(xs.subList(0, i) + xs.subList(i + 1, xs.size()));
        }
        return -findZero(xs.subList(0, xs.size() - 1));
    }
    
    /**
    xs are coefficients of a polynomial.
    findMinimum find x such that poly(x) has minimum value.
    findMinimum returns only only minimum value, even if there are many.
    Moreover, findMinimum only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> findMinimum(Arrays.asList(1, 2)) // f(x) = 1 + 2x
    1
    >>> findMinimum(Arrays.asList(-6, 11, -6, 1)) // (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1
     */
    public double findMinimum(List<Double> xs) {
        if (xs.size() == 0) {
            throw new IllegalArgumentException("empty list");
        }
        if (xs.size() % 2 == 1) {
            throw new IllegalArgumentException("odd number of coefficients");
        }
        if