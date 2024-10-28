        List<Double> result = new ArrayList<>();
        double min_difference = Double.MAX_VALUE;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double difference = Math.abs(numbers.get(i) - numbers.get(j));
                if (difference < min_difference) {
                    min_difference = difference;
                    result.set(0, numbers.get(i));
                    result.set(1, numbers.get(j));
                }
            }
        }
        return result;
    }
}

