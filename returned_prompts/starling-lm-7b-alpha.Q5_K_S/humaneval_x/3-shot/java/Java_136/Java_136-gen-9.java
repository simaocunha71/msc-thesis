        Optional<Integer> largest_negative_integer = Optional.empty();
        Optional<Integer> smallest_positive_integer = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                if (largest_negative_integer.isEmpty() || i > largest_negative_integer.get()) {
                    largest_negative_integer = Optional.of(i);
                }
            } else if (i > 0) {
                if (smallest_positive_integer.isEmpty() || i < smallest_positive_integer.get()) {
                    smallest_positive_integer = Optional.of(i);
                }
            }
        }
        return Arrays.asList(largest_negative_integer, smallest_positive_integer);
    }
}

