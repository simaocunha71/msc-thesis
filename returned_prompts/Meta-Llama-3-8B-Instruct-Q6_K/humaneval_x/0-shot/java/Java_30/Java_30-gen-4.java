    return l.stream()
             .filter(n -> n > 0)
             .collect(Collectors.toList());
}
