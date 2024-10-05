        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                if (largestNegative.isPresent()) {
                    largestNegative = Optional.of(Math.max(largestNegative.get(), i));
                } else {
                    largestNegative = Optional.of(i);
                }
            } else if (i > 0) {
                if (smallestPositive.isPresent()) {
                    smallestPositive = Optional.of(Math.min(smallestPositive.get(), i));
                } else {
                    smallestPositive = Optional.of(i);
                }
            }
        }

        return List.of(largestNegative, smallestPositive);
    }
}

