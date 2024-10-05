        for (int i = 0; i < xs.size(); i++) {
            if (xs.get(i) == 0) {
                continue;
            }
            double x = -xs.get(i) / (xs.get(i + 1));
            if (poly(xs, x) == 0) {
                return x;
            }
        }
        return 0;
    }
}

