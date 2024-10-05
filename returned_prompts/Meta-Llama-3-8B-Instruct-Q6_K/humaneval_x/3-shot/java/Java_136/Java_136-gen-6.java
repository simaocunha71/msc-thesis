        List<Optional<Integer>> result = new ArrayList<>();
        Optional<Integer> max_negative = Optional.empty();
        Optional<Integer> min_positive = Optional.empty();

        for (int num : lst) {
            if (num < 0) {
                if (max_negative.isPresent()) {
                    max_negative = Optional.of(Math.max(max_negative.get(), num));
                } else {
                    max_negative = Optional.of(num);
                }
            } else if (num > 0) {
                if (min_positive.isPresent()) {
                    min_positive = Optional.of(Math.min(min_positive.get(), num));
                } else {
                    min_positive = Optional.of(num);
                }
            }
        }
        result.add(max_negative);
        result.add(min_positive);
        return result;
    }
}

