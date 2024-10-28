        Optional<Integer> largest_negative = Optional.empty();
        Optional<Integer> smallest_positive = Optional.empty();

        for (int i : lst) {
            if (i < 0 && (Optional.empty().equals(largest_negative) || i > largest_negative.get())) {
                largest_negative = Optional.of(i);
            }
            if (i > 0 && (Optional.empty().equals(smallest_positive) || i < smallest_positive.get())) {
                smallest_positive = Optional.of(i);
            }
        }
        return List.of(largest_negative, smallest_positive);
    }
}

