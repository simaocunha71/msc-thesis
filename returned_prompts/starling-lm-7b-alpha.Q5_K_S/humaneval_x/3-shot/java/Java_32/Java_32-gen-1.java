        if (xs.size() % 2 == 1) {
            throw new IllegalArgumentException("xs must have even length");
        }

        double x = 0;
        int sign = 1;

        while (true) {
            double next_x = x - (poly(xs, x) / xs.get(xs.size() - 1));
            if (next_x == x) {
                return x;
            }
            x = next_x;
            sign *= -1;
        }
    }
}

