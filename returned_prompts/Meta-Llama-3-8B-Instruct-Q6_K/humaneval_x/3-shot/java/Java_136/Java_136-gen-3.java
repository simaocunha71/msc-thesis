        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int num : lst) {
            if (num < 0 && largestNegative.equals(Optional.empty())) {
                largestNegative = Optional.of(num);
            } else if (num < 0 && num > largestNegative.get()) {
                largestNegative = Optional.of(num);
            }

            if (num > 0 && smallestPositive.equals(Optional.empty())) {
                smallestPositive = Optional.of(num);
            } else if (num > 0 && num < smallestPositive.get()) {
                smallestPositive = Optional.of(num);
            }
        }

        return new ArrayList<>(Arrays.asList(largestNegative, smallestPositive));
    }
}

