        if (arr.isEmpty()) {
            return Optional.empty();
        }
        int signProduct = 1;
        int sumOfMagnitudes = 0;
        for (int num : arr) {
            if (num < 0) {
                signProduct *= -1;
            }
            sumOfMagnitudes += Math.abs(num);
        }
        return Optional.of(sumOfMagnitudes * signProduct);
    }
}

