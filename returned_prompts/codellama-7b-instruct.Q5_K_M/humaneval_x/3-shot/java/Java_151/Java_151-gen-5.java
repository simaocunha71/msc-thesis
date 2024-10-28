        int sum_of_odd_squares = 0;
        for (Object o : lst) {
            if (o instanceof Integer) {
                int x = (int) o;
                if (x % 2 == 1) {
                    sum_of_odd_squares += x * x;
                }
            }
        }
        return sum_of_odd_squares;
    }
}

