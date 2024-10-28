public int add(List<Integer> lst) {
    return lst.stream()
            .filter((e, i) -> i % 2 != 0 && e % 2 == 0)
            .mapToInt(Integer::intValue)
            .sum();
}