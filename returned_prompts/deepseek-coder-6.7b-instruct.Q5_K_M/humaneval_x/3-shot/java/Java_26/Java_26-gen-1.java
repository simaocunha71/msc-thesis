        Map<Integer, Integer> counts = new HashMap<>();
        return numbers.stream()
            .filter(n -> counts.merge(n, 1, Integer::sum) == 1)
            .collect(Collectors.toList());
    }
}

