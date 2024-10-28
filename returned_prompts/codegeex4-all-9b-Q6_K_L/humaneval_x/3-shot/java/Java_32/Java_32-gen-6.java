        double start = 0;
        double end = 1;
        double mid = (start + end) / 2;
        double result = poly(xs, mid);
        while (result != 0) {
            if (result > 0) {
                start = mid;
            } else {
                end = mid;
            }
            mid = (start + end) / 2;
            result = poly(xs, mid);
        }
        return mid;
    }
}

