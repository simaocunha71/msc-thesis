        double min_distance = Double.POSITIVE_INFINITY;
        int index1 = 0;
        int index2 = 0;

        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    index1 = i;
                    index2 = j;
                }
            }
        }
        return Arrays.asList(numbers.get(index1), numbers.get(index2));
    }
}

