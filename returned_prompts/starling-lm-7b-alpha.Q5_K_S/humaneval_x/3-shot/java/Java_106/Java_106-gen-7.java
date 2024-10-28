        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int value = 0;
            if (i % 2 == 0) {
                value = factorial(i);
            } else {
                for (int j = 1; j <= i; j++) {
                    value += j;
                }
            }
            result.add(value);
        }
        return result;
    }

    int factorial(int n) {
        int result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}

