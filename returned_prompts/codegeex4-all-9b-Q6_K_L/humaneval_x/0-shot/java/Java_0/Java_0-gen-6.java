public boolean hasCloseElements(List<Double> numbers, double threshold) {
    int len = numbers.size();
    for (int i = 0; i < len - 1; i++) {
        for (int j = i + 1; j < len; j++) {
            if (Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                return true;
            }
        }
    }
    return false;
}