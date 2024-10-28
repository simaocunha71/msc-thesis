        List<Optional<Integer>> result = new ArrayList<>();
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (Integer i : lst) {
            if (i < 0) {
                if (!largestNegative.isPresent() || i > largestNegative.get()) {
                    largestNegative = Optional.of(i);
                }
            }
            else {
                if (!smallestPositive.isPresent() || i < smallestPositive.get()) {
                    smallestPositive = Optional.of(i);
                }
            }
        }
        result.add(largestNegative);
        result.add(smallestPositive);
        return result;
    }
}

