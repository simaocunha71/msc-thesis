        if (arr.size() == 0) {
            return Optional.empty();
        }

        int sign_product = 1;
        long result = 0;
        for (int i : arr) {
            if (i == 0) {
                result = 0;
                break;
            } else if (i > 0) {
                result += i;
                sign_product *= 1;
            } else {
                result -= i;
                sign_product *= -1;
            }
        }
        return Optional.of((sign_product == 1) ? result : -result);
    }
}

