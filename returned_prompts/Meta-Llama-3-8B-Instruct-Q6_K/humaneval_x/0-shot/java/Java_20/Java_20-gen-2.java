    public List<Double> findClosestElements(List<Double> numbers) {
        double minDiff = Double.MAX_VALUE;
        List<Double> closestElements = new ArrayList<>();
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < minDiff) {
                minDiff = diff;
                closestElements.clear();
                closestElements.add(numbers.get(i));
                closestElements.add(numbers.get(i + 1));
            } else if (diff == minDiff) {
                closestElements.add(numbers.get(i));
                closestElements.add(numbers.get(i + 1));
            }
        }
        return closestElements;
    }
}
In this solution, we iterate through the list of numbers, calculating the difference between each pair of consecutive numbers. We keep track of the smallest difference (minDiff) and the corresponding pair of numbers. If we find a pair with a smaller difference, we update minDiff and reset the closestElements list. If we find a pair with the same smallest difference, we add it to the closestElements list. Finally, we return the closestElements list. The time complexity is O(n), where n is the length of the input list. The space complexity is O(1), since we only use a constant amount of space to store the minimum difference and the closestElements list.