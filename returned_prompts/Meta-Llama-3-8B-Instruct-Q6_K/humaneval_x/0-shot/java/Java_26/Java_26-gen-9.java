    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Boolean> seen = new HashMap<>();
        return numbers.stream()
                .filter(num -> !seen.putIfAbsent(num, true).orElse(false))
                .collect(Collectors.toList());
    }
}
