        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                result.add(fact(i));
            } else {
                result.add(sum_i(i));
            }
        }
        return result;
    }

    private int sum_i(int i) {
        int sum = 0;
        for (int j = 1; j <= i; j++) {
            sum += j;
        }
        return sum;
    }

    private int fact(int i) {
        int result = 1;
        for (int j = 2; j <= i; j++) {
            result *= j;
        }
        return result;
    }
}

