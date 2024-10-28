        double min_distance = Double.POSITIVE_INFINITY;
        int first_index = -1;
        int second_index = -1;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    first_index = i;
                    second_index = j;
                }
            }
        }
        return Arrays.asList(numbers.get(first_index), numbers.get(second_index));
    }
}

