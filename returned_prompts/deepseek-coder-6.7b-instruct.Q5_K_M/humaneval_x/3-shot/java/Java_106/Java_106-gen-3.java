        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(factorial(i));
            } else {
                result.add(sum(i));
            }
        }
        return result;
    }

    private int factorial(int i) {
        int result = 1;
        for (int j = 2; j <= i; j++) {
            result *= j;
        }
        return result;
    }

    private int sum(int i) {
        return i * (i + 1) / 2;
    }
}

