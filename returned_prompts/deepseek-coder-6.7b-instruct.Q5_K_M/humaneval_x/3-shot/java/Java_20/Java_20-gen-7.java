        Collections.sort(numbers);
        double minDifference = Double.MAX_VALUE;
        List<Double> closestPair = new ArrayList<>();

        for  (int i = 0; i < numbers.size() - 1; i++)  {
            double difference = numbers.get(i + 1) - numbers.get(i);
            if  (difference < minDifference)  {
                minDifference = difference;
                closestPair = Arrays.asList(numbers.get(i), numbers.get(i + 1));
             }
        }
        return closestPair;
     }
}

