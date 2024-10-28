        Collections.sort(numbers);
        double min_difference = Double.MAX_VALUE;
        List<Double> result = new ArrayList<>();

        for  (int i = 0; i < numbers.size() - 1; i++) {
            double difference = numbers.get(i+1) - numbers.get(i);
            if  (difference < min_difference) {
                min_difference = difference;
                result.clear();
                result.add(numbers.get(i));
                result.add(numbers.get(i+1));
             }
         }

        return result;
     }
}

