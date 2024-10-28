        if (xs.size() % 2 == 1 || xs.get(xs.size() - 1) == 0) {
            throw new IllegalArgumentException("xs must have even number of elements and last element must be non-zero");
        }

        double b = xs.get(xs.size() - 1);

        double a = xs.get(xs.size() - 2);
        double x0 = -b / a;

        double tol = 1e-15;
        double x1 = x0;
        while (Math.abs(x1 - x0) > tol) {
            x0 = x1;
            x1 = x0 - poly(xs, x0) / poly(xs, x0);
        }
        return x1;
    }
}

