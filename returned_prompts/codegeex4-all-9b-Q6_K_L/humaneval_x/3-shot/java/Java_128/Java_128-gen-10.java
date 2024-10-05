        if (arr.size() == 0) {
            return Optional.empty();
        }

        int product_of_signs = 1;
        int sum_of_magnitudes = 0;

        for (int i : arr) {
            product_of_signs *= Math.signum(i);
            sum_of_magnitudes += Math.abs(i);
        }

        return Optional.of(product_of_signs * sum_of_magnitudes);
    }
}

