        double x = xs.get(xs.size() - 1);
        double result = poly(xs, x);
        double precision = 1e-6;

        while (Math.abs(result) > precision) {
            double dx = poly(xs, x + precision);
            x -= result / dx;
            result = dx;
        }
        return x;
    }
}