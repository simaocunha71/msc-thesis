        if (arr.isEmpty()) return Optional.empty();
        int sum = 0;
        int sign = 1;
        for (int num : arr) {
            sum += Math.abs(num);
            if (num < 0) {
                sign *= -1;
            }
        }
        return Optional.of(sum * sign);
     }
}

