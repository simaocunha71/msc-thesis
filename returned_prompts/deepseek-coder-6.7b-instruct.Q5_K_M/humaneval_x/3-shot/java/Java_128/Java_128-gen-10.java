        if (arr.isEmpty()) return Optional.empty();
        int signProduct = 1;
        int magnitudeSum = 0;
        for (int num : arr) {
            if (num < 0) {
                signProduct *= -1;
            } else if (num > 0) {
                signProduct *= 1;
            }
            magnitudeSum += Math.abs(num);
        }
        return Optional.of(signProduct * magnitudeSum);
    }
}

