public int solution(List<Integer> lst) {
        return lst.stream()
                .filter((i, idx) -> i % 2 != 0 && idx % 2 == 0)
                .mapToInt(Integer::intValue)
                .sum();
    }