        Optional<Integer> max_negative = Optional.empty();
        Optional<Integer> min_positive = Optional.empty();
        for (int i : lst) {
            if (i < 0) {
                if (max_negative.isEmpty()) {
                    max_negative = Optional.of(i);
                } else if (i > max_negative.get()) {
                    max_negative = Optional.of(i);
                }
            } else if (i > 0) {
                if (min_positive.isEmpty()) {
                    min_positive = Optional.of(i);
                } else if (i < min_positive.get()) {
                    min_positive = Optional.of(i);
                }
            }
        }
        return List.of(max_negative, min_positive);
    }
}

