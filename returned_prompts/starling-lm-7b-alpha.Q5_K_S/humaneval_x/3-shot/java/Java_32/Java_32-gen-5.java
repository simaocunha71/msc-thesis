        double x0 = 1.0;
        double x1 = 0.5;
        double epsilon = 0.000001;

        while (true) {
            double x = (x0 + x1) / 2;
            double value = poly(xs, x);
            if (value == 0.0) return x;
            if (value > 0) {
                x1 = x;
            } else {
                x0 = x;
            }
        }
    }
}

