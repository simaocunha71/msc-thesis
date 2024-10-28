        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                if (largestNegative.isEmpty() || i > largestNegative.get()) {
                    largestNegative = Optional.of(i);
                }
            }
            if (i > 0) {
                if (smallestPositive.isEmpty() || i < smallestPositive.get()) {
                    smallestPositive = Optional.of(i);
                }
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}

