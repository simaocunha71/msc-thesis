    public List<Double> findClosestElements(List<Double> numbers) {
        double minDistance = Double.MAX_VALUE;
        List<Double> closestElements = new ArrayList<>();
        for (int i = 0; i < numbers.size() - 1; i++) {
            double distance = numbers.get(i + 1) - numbers.get(i);
            if (distance < minDistance) {
                minDistance = distance;
                closestElements.clear();
                closestElements.add(numbers.get(i));
                closestElements.add(numbers.get(i + 1));
            } else if (distance == minDistance) {
                closestElements.add(numbers.get(i));
                closestElements.add(numbers.get(i + 1));
            }
        }
        return closestElements;
    }  // this solution works as long as the input list is not empty and has at least two elements.

