public int doubleTheDifference(List<Object> lst) {
    return lst.stream()
        .filter(o -> o instanceof Integer)
        .map(o -> (Integer) o)
        .filter(i -> i % 2 == 0)
        .mapToInt(i -> i * i)
        .sum();
}

