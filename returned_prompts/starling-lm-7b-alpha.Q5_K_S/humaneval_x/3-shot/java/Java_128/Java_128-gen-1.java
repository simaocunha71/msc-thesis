        int sign_product = 1;
        long result = 0;
        for (int i : arr) {
            if (i == 0) result += 0;
            if (i > 0) {
                result += i;
                sign_product *= 1;
            }
            if (i < 0) {
                result -= i;
                sign_product *= -1;
            }
        }
        if (sign_product == 1) {
            return Optional.of(result);
        } else {
            return Optional.empty();
        }
    }
}

