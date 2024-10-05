        double left = 0;
        double right = xs.size() - 1;
        while (right - left > 0.01) {
            double mid = (left + right) / 2;
            double result = poly(xs, mid);
            if (result == 0) {
                return mid;
            } else if (result > 0) {
                right = mid;
            } else {
                left = mid;
            }
        }
        return (left + right) / 2;
    }
}

