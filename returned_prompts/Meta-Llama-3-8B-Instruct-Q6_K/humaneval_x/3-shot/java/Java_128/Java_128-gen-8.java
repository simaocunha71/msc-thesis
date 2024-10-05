        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int sign_product = 1;
        int sum_of_magnitudes = 0;

        for (int num : arr) {
            sign_product *= Math.signum(num);
            sum_of_magnitudes += Math.abs(num);
        }

        return Optional.of(sum_of_magnitudes * sign_product);
    }
}

