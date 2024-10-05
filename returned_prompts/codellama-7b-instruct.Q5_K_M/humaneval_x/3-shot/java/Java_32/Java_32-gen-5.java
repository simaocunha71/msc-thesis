        if (xs.size() % 2 == 1 || Math.abs(xs.get(xs.size() - 1)) < 1e-10) {
            throw new RuntimeException("xs must have even number of coefficients and the largest nonzero one");
        }
        double x0 = -xs.get(xs.size() - 2) / xs.get(xs.size() - 1);
        double x1 = 0;
        while (Math.abs(x0 - x1) > 1e-10) {
            x1 = x0;
            x0 = x1 - poly(xs, x1) / poly(xs, x1 * x1);
        }
        return x0;

    }
}

