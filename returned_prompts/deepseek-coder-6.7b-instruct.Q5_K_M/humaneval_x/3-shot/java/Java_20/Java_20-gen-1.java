        Collections.sort(numbers);
        double min_difference = Double.MAX_VALUE;
        double min_first_number = numbers.get(0);
        double min_second_number = numbers.get(1);

        for  (int i = 0; i < numbers.size() - 1; i++) {
            double difference = numbers.get(i+1) - numbers.get(i);
            if  (difference < min_difference)  {
                min_difference = difference;
                min_first_number = numbers.get(i);
                min_second_number = numbers.get(i+1);
             }
         }
        return Arrays.asList(min_first_number, min_second_number);
     }
}

