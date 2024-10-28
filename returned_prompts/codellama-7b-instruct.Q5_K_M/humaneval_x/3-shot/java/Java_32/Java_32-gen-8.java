        if (xs.size() % 2 != 0) {
            throw new IllegalArgumentException("xs should have even number of coefficients");
        }
        double largest_coefficient = xs.get(xs.size() / 2);
        if (largest_coefficient == 0) {
            throw new IllegalArgumentException("largest coefficient should not be zero");
        }

        double left_bound = -largest_coefficient;
        double right_bound = -largest_coefficient;

        for (int i = 0; i < xs.size() / 2; i++) {
            if (xs.get(i) > 0) {
                left_bound = i;
            }
            if (xs.get(xs.size() - i - 1) > 0) {
                right_bound = i;
            }
        }

        return bisect(xs, left_bound, right_bound);
    }

    private double bisect(List<Double> xs, double left_bound, double right_bound) {
        while (right_bound - left_bound > 1e-6) {
            double mid = (left_bound + right_bound) / 2;
            if (poly(xs, mid) > 0) {
                right_bound = mid;
            } else {
                left_bound = mid;
            }
        }
        return (left_bound + right_bound) / 2;
    }
}

