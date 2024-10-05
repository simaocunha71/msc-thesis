        if (arr.size() == 0) return Optional.empty();

        int product_sign = 1;
        int sum_magnitudes = 0;

        for (int num : arr) {
            product_sign *= Math.signum(num);
            sum_magnitudes += Math.abs(num);
        }
        return Optional.of(product_sign * sum_magnitudes);
    }
}

