        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (Integer number : lst) {
            if (number < 0 && (largestNegative.isEmpty() || number > largestNegative.get())) {
                largestNegative = Optional.of(number);
            } else if (number > 0 && (smallestPositive.isEmpty() || number < smallestPositive.get())) {
                smallestPositive = Optional.of(number);
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}

