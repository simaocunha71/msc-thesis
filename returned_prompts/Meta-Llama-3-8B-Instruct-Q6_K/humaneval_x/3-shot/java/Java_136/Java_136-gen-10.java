        Optional<Integer> maxNegative = Optional.empty();
        Optional<Integer> minPositive = Optional.empty();
        for (int i : lst) {
            if (i < 0 && !maxNegative.isPresent() || i > maxNegative.get()) {
                maxNegative = Optional.of(i);
            }
            if (i > 0 && !minPositive.isPresent() || i < minPositive.get()) {
                minPositive = Optional.of(i);
            }
        }
        return List.of(maxNegative, minPositive);
    }
}

