        if (xs.size() % 2 == 1) {
            throw new RuntimeException("xs must have even number of coefficients");
        }
        double x = xs.get(xs.size() - 1); // start from largest coefficient
        double result = poly(xs, x);
        while (Math.abs(result) > 0.0001) {
            x = -result / poly(xs, x);
            result = poly(xs, x);
        }
        return x;
    }
}

