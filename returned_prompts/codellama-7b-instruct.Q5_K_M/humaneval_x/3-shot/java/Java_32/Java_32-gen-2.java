        if (xs.size() % 2 == 1 || xs.get(0) == 0) {
            throw new IllegalArgumentException("Can't find zero");
        }
        double x1 = -xs.get(0) / xs.get(1);
        double x2 = -xs.get(0) / xs.get(3);
        if (x1 == x2) {
            return x1;
        } else if (x1 > x2) {
            return findZero(xs.subList(2, xs.size()));
        } else {
            return findZero(xs.subList(0, xs.size() - 2));
        }
    }
}

