        Optional<Integer> largest = Optional.empty();
        Optional<Integer> smallest = Optional.empty();

        for (Integer i : lst) {
            if (i < 0) {
                if (largest.isEmpty() || i > largest.get()) {
                    largest = Optional.of(i);
                }
            } else if (i > 0) {
                if (smallest.isEmpty() || i < smallest.get()) {
                    smallest = Optional.of(i);
                }
            }
        }
        return Arrays.asList(largest, smallest);
    }
}

