        if (arr.isEmpty()) {
            return Optional.empty();
        }
        int sign_product = 1;
        int sum_of_magnitudes = 0;
        for (int num : arr) {
            if (num == 0) {
                return Optional.of(0);
            }
            sign_product *= Math.signum(num);
            sum_of_magnitudes += Math.abs(num);
        }
        return Optional.of(sign_product * sum_of_magnitudes);
    }
}

