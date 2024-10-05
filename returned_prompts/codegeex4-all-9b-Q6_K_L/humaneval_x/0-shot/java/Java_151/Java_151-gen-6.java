public int doubleTheDifference(List<Object> lst) {
    return lst.stream()
            .filter(n -> n instanceof Integer && (Integer) n % 2 != 0 && (Integer) n > 0)
            .mapToInt(n -> (Integer) n * (Integer) n)
            .sum();
}