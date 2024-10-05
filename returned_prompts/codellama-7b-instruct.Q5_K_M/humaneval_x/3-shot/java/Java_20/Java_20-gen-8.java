        double smallest_difference = Double.MAX_VALUE;
        List<Double> result = new ArrayList<>();

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double difference = Math.abs(numbers.get(i) - numbers.get(j));
                if (difference < smallest_difference) {
                    smallest_difference = difference;
                    result.clear();
                    result.add(numbers.get(i));
                    result.add(numbers.get(j));
                }
            }
        }
        return result;
    }
}

