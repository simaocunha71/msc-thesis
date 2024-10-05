        int sum = 1;
        int factorial = 1;
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                factorial = factorial * i;
                list.add(factorial);
            } else {
                sum = sum + i;
                list.add(sum);
            }
        }
        return list;
    }
}
