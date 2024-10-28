        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (Integer num : lst) {
            if (num < 0) {
                largestNegative = Optional.of(num);
            } else if (num > 0) {
                smallestPositive = Optional.of(num);
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}

