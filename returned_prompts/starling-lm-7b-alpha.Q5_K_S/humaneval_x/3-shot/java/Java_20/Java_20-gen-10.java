        Collections.sort(numbers);
        int min_distance_index = 0;
        double min_distance = Double.MAX_VALUE;
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    min_distance_index = i;
                }
            }
        }
        return Arrays.asList(numbers.get(min_distance_index), numbers.get(min_distance_index + 1));
    }
}

