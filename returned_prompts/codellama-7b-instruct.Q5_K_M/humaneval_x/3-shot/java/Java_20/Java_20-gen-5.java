        List<Double> result = new ArrayList<>();
        if (numbers.size() == 2) {
            result.add(numbers.get(0));
            result.add(numbers.get(1));
            return result;
        }

        double smallest_distance = Double.MAX_VALUE;
        int smallest_distance_index_0 = -1;
        int smallest_distance_index_1 = -1;

        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < smallest_distance) {
                    smallest_distance = distance;
                    smallest_distance_index_0 = i;
                    smallest_distance_index_1 = j;
                }
            }
        }
        result.add(numbers.get(smallest_distance_index_0));
        result.add(numbers.get(smallest_distance_index_1));
        return result;
    }
}

