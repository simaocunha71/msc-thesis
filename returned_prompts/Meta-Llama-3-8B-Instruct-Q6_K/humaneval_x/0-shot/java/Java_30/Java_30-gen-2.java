public List<Integer> getPositive(List<Integer> l) {
    return l.stream()
            .filter(num -> num > 0)
            .collect(Collectors.toList());
}
