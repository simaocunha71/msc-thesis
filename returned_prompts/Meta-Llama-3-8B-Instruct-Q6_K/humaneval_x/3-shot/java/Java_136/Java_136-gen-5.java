        Optional<Integer> maxNegative = Optional.empty();
        Optional<Integer> minPositive = Optional.empty();
        for (int num : lst) {
            if (num < 0) {
                if (!maxNegative.isPresent() || num > maxNegative.get()) {
                    maxNegative = Optional.of(num);
                }
            } else if (num > 0) {
                if (!minPositive.isPresent() || num < minPositive.get()) {
                    minPositive = Optional.of(num);
                }
            }
        }
        return List.of(maxNegative, minPositive);
    }
} 

