        List<Double> result = new ArrayList<>();
        double min_distance = Double.MAX_VALUE;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    result.clear();
                    result.add(Math.min(numbers.get(i), numbers.get(j)));
                    result.add(Math.max(numbers.get(i), numbers.get(j)));
                }
            }
        }
        return result;
    }
}

