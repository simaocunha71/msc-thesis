        int sum_of_squares = 0;
        int sum_of_odd_nums = 0;

        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int num = (Integer) obj;
                if (num % 2 == 1) {
                    sum_of_odd_nums += num * num;
                }
            }
        }

        return sum_of_odd_nums;
    }
}

