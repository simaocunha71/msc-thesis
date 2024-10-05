        List<Double> result = new ArrayList<>();
        double current_distance = Double.MAX_VALUE;
        double current_result = 0.0;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < current_distance) {
                    current_distance = distance;
                    result.set(0, numbers.get(i));
                    result.set(1, numbers.get(j));
                }
            }
        }
        return result;
    }
}

