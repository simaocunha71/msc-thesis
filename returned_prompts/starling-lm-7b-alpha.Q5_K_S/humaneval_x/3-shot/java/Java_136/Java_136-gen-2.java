        Optional<Integer> largest_negative = Optional.empty();
        Optional<Integer> smallest_positive = Optional.empty();

        for (int i : lst) {
            if (i < 0) largest_negative = Optional.of(i);
            if (i > 0) smallest_positive = Optional.of(i);
        }
        return Arrays.asList(largest_negative, smallest_positive);
    }
}

