        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add((int) factorial(i));
            } else {
                result.add(sum_from_1_to_i(i));
            }
        }
        return result;
    }

    public long factorial(int n) {
        if (n == 1) return 1;
        return n * factorial(n - 1);
    }

    public int sum_from_1_to_i(int i) {
        int result = 0;
        for (int j = 1; j <= i; j++) {
            result += j;
        }
        return result;
    }
}

