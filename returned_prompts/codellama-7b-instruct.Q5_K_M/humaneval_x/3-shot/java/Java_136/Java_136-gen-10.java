        Optional<Integer> largest_negative = Optional.empty();
        Optional<Integer> smallest_positive = Optional.empty();

        for (Integer i : lst) {
            if (i < 0) {
                if (largest_negative.isEmpty() || i > largest_negative.get()) {
                    largest_negative = Optional.of(i);
                }
            } else {
                if (smallest_positive.isEmpty() || i < smallest_positive.get()) {
                    smallest_positive = Optional.of(i);
                }
            }
        }

        return Arrays.asList(largest_negative, smallest_positive);
    }
}

