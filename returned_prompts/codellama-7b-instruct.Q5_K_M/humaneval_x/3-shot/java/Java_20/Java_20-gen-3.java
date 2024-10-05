        double min_distance = Double.MAX_VALUE;
        int min_index_1 = 0;
        int min_index_2 = 0;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    min_index_1 = i;
                    min_index_2 = j;
                }
            }
        }
        return Arrays.asList(numbers.get(min_index_1), numbers.get(min_index_2));
    }
}

