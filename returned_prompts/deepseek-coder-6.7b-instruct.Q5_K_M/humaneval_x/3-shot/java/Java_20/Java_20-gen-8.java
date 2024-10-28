        Collections.sort(numbers);
        double min_difference = Double.MAX_VALUE;
        List<Double> closest_pair = new ArrayList<>();

        for  (int i = 0; i < numbers.size() - 1; i++) {
            double difference = numbers.get(i + 1) - numbers.get(i);

            if  (difference < min_difference) {
                min_difference = difference;
                closest_pair.clear();
                closest_pair.add(numbers.get(i));
                closest_pair.add(numbers.get(i + 1));
             }
         }
         return closest_pair;
     }
 }

