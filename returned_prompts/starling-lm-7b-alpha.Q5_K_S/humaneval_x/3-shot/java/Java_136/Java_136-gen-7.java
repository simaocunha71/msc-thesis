        Optional<Integer> largest_negative = Optional.empty();
        Optional<Integer> smallest_positive = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                if (largest_negative.isEmpty()) {
                    largest_negative = Optional.of(i);
                } else {
                    largest_negative = Optional.of(Math.max(i, largest_negative.get()));
                }
            } else {
                if (smallest_positive.isEmpty()) {
                    smallest_positive = Optional.of(i);
                } else {
                    smallest_positive = Optional.of(Math.min(i, smallest_positive.get()));
                }
            }
        }

        return Arrays.asList(largest_negative, smallest_positive);
    }
}

