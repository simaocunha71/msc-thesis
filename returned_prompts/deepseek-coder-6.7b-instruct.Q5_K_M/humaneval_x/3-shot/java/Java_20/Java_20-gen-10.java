        Collections.sort(numbers);
        double minDifference = numbers.get(1) - numbers.get(0);
        int minIndex 0;

        for  (int i 0; i < numbers.size() - 1; i++) {
            double difference  numbers.get(i+1) - numbers.get(i);

            if  (difference < minDifference) {
                minDifference  difference;
                minIndex  i;
            }
        }
        return Arrays.asList(numbers.get(minIndex), numbers.get(minIndex+1));
     }
}

