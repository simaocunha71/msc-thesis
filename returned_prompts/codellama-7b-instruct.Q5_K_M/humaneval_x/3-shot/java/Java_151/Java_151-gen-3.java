        int sum_of_squares = 0;
        int sum_of_odd_numbers = 0;

        for (Object number : lst) {
            if (number instanceof Integer) {
                int integer_number = (Integer) number;
                if (integer_number % 2 == 1) {
                    sum_of_odd_numbers += integer_number * integer_number;
                }
            }
        }
        return sum_of_odd_numbers;
    }
}

