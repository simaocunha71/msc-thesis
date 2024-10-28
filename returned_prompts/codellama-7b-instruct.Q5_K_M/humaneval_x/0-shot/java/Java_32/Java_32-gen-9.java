    for (int i = 0; i < xs.size() - 1; i++) {
        if (xs.get(i) == 0) {
            continue A;
        }
        if (xs.get(i) < 0) {
            return findZero(xs.subList(i + 1, xs.size()));
        }
    }
    return -xs.get(0) / xs.get(1);
