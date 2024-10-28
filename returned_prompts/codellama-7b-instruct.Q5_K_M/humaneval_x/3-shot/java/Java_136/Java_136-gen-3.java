        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                if (largestNegative.isEmpty()) {
                    largestNegative = Optional.of(i);
                } else if (i > largestNegative.get()) {
                    largestNegative = Optional.of(i);
                }
            } else if (i > 0) {
                if (smallestPositive.isEmpty()) {
                    smallestPositive = Optional.of(i);
                } else if (i < smallestPositive.get()) {
                    smallestPositive = Optional.of(i);
                }
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}

