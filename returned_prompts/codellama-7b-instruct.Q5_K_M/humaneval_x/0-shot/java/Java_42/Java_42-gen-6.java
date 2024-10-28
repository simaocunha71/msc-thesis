        List<Integer> r = l.stream()
            .map(i -> i + 1)
            .collect(Collectors.toList());
        return r;
    }
}
