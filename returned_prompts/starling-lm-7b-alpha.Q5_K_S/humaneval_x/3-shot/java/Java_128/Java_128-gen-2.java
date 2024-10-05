        if (arr.size() == 0) return Optional.empty();
        long result = 0;
        long sign = 1;
        for (int a : arr) {
            if (a == 0) {
                sign *= 0;
            } else if (a < 0) {
                sign *= -1;
            } else {
                sign *= 1;
            }
            result += Math.abs(a);
        }
        return Optional.of((int) result * sign);
    }
}


```