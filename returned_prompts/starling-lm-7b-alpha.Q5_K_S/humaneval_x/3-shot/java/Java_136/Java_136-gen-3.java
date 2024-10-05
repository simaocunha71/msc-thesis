        Optional<Integer> largest_negative = Optional.empty();
        Optional<Integer> smallest_positive = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                if (largest_negative.isEmpty()) {
                    largest_negative = Optional.of(i);
                } else if (i > largest_negative.get()) {
                    largest_negative = Optional.of(i);
                }
            } else if (i > 0) {
                if (smallest_positive.isEmpty()) {
                    smallest_positive = Optional.of(i);
                } else if (i < smallest_positive.get()) {
                    smallest_positive = Optional.of(i);
                }
            }
        }
        return List.of(largest_negative, smallest_positive);
    }
}


