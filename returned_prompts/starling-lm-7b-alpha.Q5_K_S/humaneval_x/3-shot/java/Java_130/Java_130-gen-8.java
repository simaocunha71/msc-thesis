        List<Integer> result = new ArrayList<>();
        result.add(3);
        result.add(1);
        result.add(2);
        if (n == 0) return result;
        if (n == 1) return result;
        if (n == 2) return result;

        int n_minus_3 = 3;
        int n_minus_2 = 1;
        int n_minus_1 = 2;
        while (result.size() < n + 1) {
            int current_tribonacci = n_minus_1 + n_minus_2 + n_minus_3;
            result.add(current_tribonacci);

            int current_n_minus_2 = n_minus_1;
            int current_n_minus_1 = n_minus_2;
            int current_n_minus_3 = n_minus_3;
            n_minus_3 = current_n_minus_2;
            n_minus_2 = current_n_minus_1;
            n_minus_1 = current_n_minus_3;
        }
        return result;
    }
}

