        if (xs.size() % 2 == 1 || Math.abs(xs.get(xs.size() - 1)) < 1e-10) {
            throw new IllegalArgumentException("xs must have even number of coefficients and largest non zero coefficient");
        }
        double left = -1e100;
        double right = 1e100;

        while (right - left > 1e-10) {
            double mid = (left + right) / 2;
            if (poly(xs, mid) < 0) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return (left + right) / 2;
    }
}

