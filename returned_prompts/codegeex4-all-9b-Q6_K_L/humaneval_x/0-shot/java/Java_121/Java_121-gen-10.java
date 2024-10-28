public int solution(List<Integer> lst) {
    return lst.stream()
        .filter((x, i) -> i % 2 == 0 && x % 2 != 0)
        .mapToInt(Integer::intValue)
        .sum();
}