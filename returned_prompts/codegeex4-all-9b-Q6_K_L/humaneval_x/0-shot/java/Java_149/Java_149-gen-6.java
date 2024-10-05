public List<String> listSort(List<String> lst) {
    return lst.stream()
            .filter(s -> s.length() % 2 == 0)
            .sorted(Comparator.comparingInt(String::length).thenComparing(String::compareTo))
            .collect(Collectors.toList());
}