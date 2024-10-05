public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst) {
    List<Optional<Integer>> result = new ArrayList<>();
    Optional<Integer> largestNegative = Optional.empty();
    Optional<Integer> smallestPositive = Optional.empty();
    for (int i = 0; i < lst.size(); i++) {
        if (lst.get(i) < 0) {
            if (largestNegative.isEmpty()) {
                largestNegative = Optional.of(lst.get(i));
            } else {
                if (lst.get(i) > largestNegative.get()) {
                    largestNegative = Optional.of(lst.get(i));
                }
            }
        } else if (lst.get(i) > 0) {
            if (smallestPositive.isEmpty()) {
                smallestPositive = Optional.of(lst.get(i));
            } else {
                if (lst.get(i) < smallestPositive.get()) {
                    smallestPositive = Optional.of(lst.get(i));
                }
            }
        }
    }
    result.add(largestNegative);
    result.add(smallestPositive);
    return result;
}
