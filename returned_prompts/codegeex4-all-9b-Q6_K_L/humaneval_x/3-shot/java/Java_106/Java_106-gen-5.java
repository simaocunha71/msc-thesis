        List<Integer> result = new ArrayList<>();
        int sum = 1;
        int factorial = 1;

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                factorial *= i;
                result.add(factorial);
            } else {
                sum += i;
                result.add(sum);
            }
        }

        return result;
    }
}

