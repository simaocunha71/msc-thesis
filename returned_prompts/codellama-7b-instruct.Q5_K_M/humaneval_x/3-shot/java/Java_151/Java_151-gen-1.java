        int sum_of_squares = 0;
        int sum_of_odd_ints = 0;

        if (lst.size() == 0) return 0;

        for (Object o : lst) {

            if (o instanceof Integer) {

                int num = (Integer) o;
                if (num % 2 == 1) {
                    sum_of_odd_ints += num;
                }
            }
        }

        for (Object o : lst) {
            if (o instanceof Integer) {
                sum_of_squares += Math.pow(Math.abs((Integer) o), 2);
            }
        }

        return Math.abs(sum_of_squares - Math.pow(sum_of_odd_ints, 2));
    }
}

