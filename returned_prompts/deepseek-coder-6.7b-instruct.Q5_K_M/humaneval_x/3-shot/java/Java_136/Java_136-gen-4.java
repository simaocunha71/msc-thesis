        Optional<Integer> maxNegative = Optional.empty();
        Optional<Integer> minPositive = Optional.empty();

        for (Integer num : lst) {
            if (num > 0) {
                if (!minPositive.isPresent() || num < minPositive.get()) {
                    minPositive = Optional.of(num);
                }
            } else if (num < 0) {
                if (!maxNegative.isPresent() || num > maxNegative.get()) {
                    maxNegative = Optional.of(num);
                }
            }
        }

        return Arrays.asList(maxNegative, minPositive);
    }
}

