    public List<Double> findClosestElements(List<Double> numbers) {
        double minDiff = Double.MAX_VALUE;
        double closest1 = 0.0;
        double closest2 = 0.0;

        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < minDiff) {
                minDiff = diff;
                closest1 = numbers.get(i);
                closest2 = numbers.get(i + 1);
            }
        }

        List<Double> result = new ArrayList<>();
        result.add(closest1);
        result.add(closest2);

        return result;
    }