        if (arr.size() == 0) {
            return Optional.empty();
        } else {
            long result = 0;
            long sign = 1;
            for (int n : arr) {
                result += Math.abs(n) * sign;
                if (n < 0) {
                    sign *= -1;
                }
            }
            return Optional.of((int)result);
        }
    }
}

