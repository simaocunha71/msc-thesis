        if (arr.size() == 0) return Optional.empty();
        long sum = 0;
        long sign = 1;
        for (int x : arr) {
            if (x == 0) {
                sign *= 0;
            } else if (x < 0) {
                sign *= -1;
            } else {
                sign *= 1;
            }
            sum += Math.abs(x);
        }
        if (sign == 0) {
            return Optional.empty();
        }
        return Optional.of((int) (sign * sum));
    }
}

