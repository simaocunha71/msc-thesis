        Set<Integer> seen = new HashSet<>();
        return numbers.stream()
            .filter(n -> seen.add(n))
            .collect(Collectors.toList());
    }
}

