        int sum_of_odd_squares = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int number = (Integer) obj;
                if (number % 2 == 1) {
                    sum_of_odd_squares += number * number;
                }
            }
        }
        return sum_of_odd_squares;
    }
}

