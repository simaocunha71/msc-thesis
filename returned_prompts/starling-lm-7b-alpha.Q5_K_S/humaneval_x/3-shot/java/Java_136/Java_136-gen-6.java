        OptionalInt max = lst.stream().filter(i -> i < 0).max();
        OptionalInt min = lst.stream().filter(i -> i > 0).min();

        return Arrays.asList(max.map(OptionalInt::get), min.map(OptionalInt::get));
    }
}

