        double x = 0;
        double step = 0.01;
        double result = poly(xs, x);
        while (result != 0) {
            x += step;
            result = poly(xs, x);
        }
        return x;
    }
}

