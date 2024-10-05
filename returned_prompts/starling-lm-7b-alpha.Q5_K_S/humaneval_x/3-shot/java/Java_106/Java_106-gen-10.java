        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int factorial = 1;
            for (int j = 1; j <= i; j++) {
                factorial *= j;
            }
            if (i % 2 == 0) {
                result.add(factorial);
            } else {
                result.add(factorial);
            }
        }
        return result;
    }
}

