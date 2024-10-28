        OptionalInt largest_negative = lst.stream().filter(i -> i < 0).max();
        OptionalInt smallest_positive = lst.stream().filter(i -> i > 0).min();
        return Arrays.asList(largest_negative.map(OptionalInt::get), smallest_positive.map(OptionalInt::get));
    }
}

