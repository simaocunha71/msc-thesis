        Optional<Integer> largest = Optional.empty();
        Optional<Integer> smallest = Optional.empty();

        for (int i : lst) {
            if (i < 0) largest = Optional.of(Math.max(largest.orElse(Integer.MIN_VALUE), i));
            if (i > 0) smallest = Optional.of(Math.min(smallest.orElse(Integer.MAX_VALUE), i));
        }
        return Arrays.asList(largest, smallest);
    }
}

