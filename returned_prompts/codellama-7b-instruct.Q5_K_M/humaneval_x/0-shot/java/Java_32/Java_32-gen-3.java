        for (int i = 0; i < xs.size(); i++) {
            if (i % 2 == 0) {
                continue A;
            }
            if (xs.get(i) != 0) {
                throw new RuntimeException("There are too many coefficients in the list");
            }
        }

        double x = 1;
        while (poly(xs, x) != 0) {
            x++;
        }

        return x - 1;
    }
}
