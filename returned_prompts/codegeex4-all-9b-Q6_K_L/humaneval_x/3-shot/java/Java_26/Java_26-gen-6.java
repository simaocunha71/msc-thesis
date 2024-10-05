        Set<Integer> unique = new HashSet<>();

        return numbers.stream()
                .filter(n -> unique.add(n))
                .collect(Collectors.toList());
    }
}

