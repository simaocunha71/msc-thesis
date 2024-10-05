        Optional<Integer> largest = Optional.empty(), smallest = Optional.empty();
        for (Integer i : lst) {
            if (i < 0) {
                if (!largest.isPresent() || i > largest.get()) {
                    largest = Optional.of(i);
                }
            } else if (i > 0) {
                if (!smallest.isPresent() || i < smallest.get()) {
                    smallest = Optional.of(i);
                }
            }
        }
        return Arrays.asList(largest, smallest);
    }
}

