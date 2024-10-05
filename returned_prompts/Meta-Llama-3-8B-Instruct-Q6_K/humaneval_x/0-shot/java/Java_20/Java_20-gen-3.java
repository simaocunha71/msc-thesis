    public List<Double> findClosestElements(List<Double> numbers) {
        double minDiff = Double.MAX_VALUE;
        double closestElements = numbers.get(0);
        List<Double> result = new ArrayList<>();
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < minDiff) {
                minDiff = diff;
                result.clear();
                result.add(numbers.get(i));
                result.add(numbers.get(i + 1));
            } else if (diff == minDiff) {
                result.clear();
                result.add(numbers.get(i));
                result.add(numbers.get(i + 1));
            }
        }
        return result;
    }