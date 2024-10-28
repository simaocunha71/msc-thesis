        Optional<Integer> max = lst.stream().filter(i -> i < 0).max(Comparator.naturalOrder());
        Optional<Integer> min = lst.stream().filter(i -> i > 0).min(Comparator.naturalOrder());
        return Arrays.asList(max, min);
    }
}

