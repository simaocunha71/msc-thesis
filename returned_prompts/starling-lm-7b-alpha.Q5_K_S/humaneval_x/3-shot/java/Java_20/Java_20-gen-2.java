        Collections.sort(numbers);
        double min_distance = Double.MAX_VALUE;
        List<Double> result = null;
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    result = Arrays.asList(numbers.get(i), numbers.get(j));
                }
            }
        }
        return result;
    }
}

