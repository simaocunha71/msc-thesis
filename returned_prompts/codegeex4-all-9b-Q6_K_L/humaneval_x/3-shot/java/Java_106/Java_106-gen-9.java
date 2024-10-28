        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                result.add(i);
            } else {
                int factorial = 1;
                for (int j = 2; j <= i; j++) {
                    factorial *= j;
                }
                result.add(factorial);
            }
        }
        return result;
    }
}

