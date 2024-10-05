        Collections.sort(numbers);
        double min_difference = Double.MAX_VALUE;
        double min_first = 0.0, min_second = 0.0;

        for  (int i = 0; i < numbers.size() - 1; i++) {
            double difference = numbers.get(i + 1) - numbers.get(i);

            if  (difference < min_difference) {
                min_difference = difference;
                min_first = numbers.get(i);
                min_second = numbers.get(i + 1);
            }
        }
        return Arrays.asList(min_first, min_second);
    }
}

