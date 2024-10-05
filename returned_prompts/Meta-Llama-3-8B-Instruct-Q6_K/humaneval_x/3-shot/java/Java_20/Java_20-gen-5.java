        double min_distance = Double.MAX_VALUE;
        Double closest_pair[] = new Double[2];

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    closest_pair[0] = numbers.get(i);
                    closest_pair[1] = numbers.get(j);
                }
            }
        }
        List<Double> result = new ArrayList<>();
        result.add(closest_pair[0]);
        result.add(closest_pair[1]);
        return result;
    }
}