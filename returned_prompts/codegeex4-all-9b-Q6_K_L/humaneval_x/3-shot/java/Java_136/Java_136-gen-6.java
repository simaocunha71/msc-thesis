        Optional<Integer> min = lst.stream()
            .filter(i -> i > 0)
            .min(Integer::compareTo);

        Optional<Integer> max = lst.stream()
            .filter(i -> i < 0)
            .max(Integer::compareTo);

        return Arrays.asList(min, max);
    }
}

