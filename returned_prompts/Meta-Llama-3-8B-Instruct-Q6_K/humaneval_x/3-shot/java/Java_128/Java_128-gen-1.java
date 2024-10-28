        if (arr.isEmpty()) {
            return Optional.empty();
        }
        int sign_product = 1;
        int sum_of_magnitudes = 0;
        for (int num : arr) {
            if (num > 0) {
                sign_product *= 1;
            } else if (num < 0) {
                sign_product *= -1;
            } else {
                sign_product *= 0;
            }
            sum_of_magnitudes += Math.abs(num);
        }
        return Optional.of(sum_of_magnitudes * sign_product);
    }
}

