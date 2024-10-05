        if (arr.size() == 0) return Optional.empty();

        int sign_product = 1;
        long result = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == 0) {
                sign_product *= 0;
            } else {
                result += Math.abs(arr.get(i)) * sign_product;
                sign_product *= ((arr.get(i) > 0) ? 1 : -1);
            }
        }
        return Optional.of((int) result);
    }
}

