        if (arr.isEmpty()) return Optional.empty();

        int prod = 1;
        int sum = 0;

        for (int num : arr) {
            if (num < 0) {
                prod *= -1;
                sum += Math.abs(num);
            } else if (num > 0) {
                sum += num;
            }
        }

        return Optional.of(prod * sum);
     }
}

