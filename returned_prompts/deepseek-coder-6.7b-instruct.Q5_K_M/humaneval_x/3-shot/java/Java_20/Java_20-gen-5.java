        Collections.sort(numbers);
        double minDifference = Double.MAX_VALUE;
        double minNumber1 = 0.0;
        double minNumber2 = 0.0;

        for (int i = 0; i < numbers.size() - 1; i++) {
            double difference = numbers.get(i + 1) - numbers.get(i);
            if (difference < minDifference) {
                minDifference = difference;
                minNumber1 = numbers.get(i);
                minNumber2 = numbers.get(i + 1);
            }
        }

        return Arrays.asList(minNumber1, minNumber2);
     }
}

