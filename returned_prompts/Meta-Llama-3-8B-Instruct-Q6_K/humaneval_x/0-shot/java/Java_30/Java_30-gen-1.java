public List<Integer> getPositive(List<Integer> l) {
    return l.stream()
            .filter(i -> i > 0)
            .collect(Collectors.toList());
}