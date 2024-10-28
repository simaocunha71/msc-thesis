        if (arr.size() == 0) return Optional.empty();
        int productSign = 1;
        int sum = 0;
        for (int num : arr) {
            if (num < 0) {
                productSign *= -1;
                sum += Math.abs(num);
            } else if (num > 0) {
                sum += num;
            }
        }
        return Optional.of(productSign * sum);
    }
}

