        if (arr.isEmpty()) return Optional.empty();

        int sumOfMagnitudes = 0;
        int signProduct = 1;

        for (int num : arr) {
            if (num < 0) {
                signProduct *= -1;
                sumOfMagnitudes += Math.abs(num);
            } else if (num > 0) {
                sumOfMagnitudes += num;
            }
        }

        return Optional.of(signProduct * sumOfMagnitudes);
    }
}

