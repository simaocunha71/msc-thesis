        List<Double> result = new ArrayList<>();
        double smallest_distance = Double.MAX_VALUE;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < smallest_distance) {
                    smallest_distance = distance;
                    result.clear();
                    result.add(numbers.get(i));
                    result.add(numbers.get(j));
                }
            }
        }
        return result;
    }
}

