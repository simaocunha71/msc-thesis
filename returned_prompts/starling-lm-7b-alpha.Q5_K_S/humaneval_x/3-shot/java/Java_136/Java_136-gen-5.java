        Optional<Integer> max_neg = Optional.empty();
        Optional<Integer> min_pos = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                max_neg = Optional.of(i);
            } else if (i > 0) {
                min_pos = Optional.of(i);
            }
        }
        return Arrays.asList(max_neg, min_pos);
    }
}

