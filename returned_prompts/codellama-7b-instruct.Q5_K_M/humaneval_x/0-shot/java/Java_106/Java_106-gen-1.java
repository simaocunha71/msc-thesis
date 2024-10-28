        List<Integer> result = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(getFactorial(i));
            } else {
                result.add(getSum(i));
            }
        }
        return result;
    }

    private int getFactorial(int num) {
        int result = 1;
        for (int i = 1; i <= num; i++) {
            result *= i;
        }
        return result;
    }

    private int getSum(int num) {
        int result = 0;
        for (int i = 1; i <= num; i++) {
            result += i;
        }
        return result;
    }
}
