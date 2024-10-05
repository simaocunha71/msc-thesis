        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int num : lst) {
            if (num < 0) {
                if (!largestNegative.isPresent() || num > largestNegative.get()) {
                    largestNegative = Optional.of(num);
                }
            } else if (num > 0) {
                if (!smallestPositive.isPresent() || num < smallestPositive.get()) {
                    smallestPositive = Optional.of(num);
                }
            }
        }

        return new ArrayList<>(Arrays.asList(largestNegative, smallestPositive));
    }
}

