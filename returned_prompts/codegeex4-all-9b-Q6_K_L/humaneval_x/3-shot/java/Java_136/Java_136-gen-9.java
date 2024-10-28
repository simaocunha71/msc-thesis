        Optional<Integer> largest = Optional.empty();
        Optional<Integer> smallest = Optional.empty();
        boolean hasNegative = false;
        boolean hasPositive = false;

        for (Integer i : lst) {
            if (i < 0) {
                hasNegative = true;
                if (!largest.isPresent() || i > largest.get()) {
                    largest = Optional.of(i);
                }
            } else if (i > 0) {
                hasPositive = true;
                if (!smallest.isPresent() || i < smallest.get()) {
                    smallest = Optional.of(i);
                }
            }
        }

        if (!hasNegative) largest = Optional.empty();
        if (!hasPositive) smallest = Optional.empty();

        return Arrays.asList(largest, smallest);
    }
}

