        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add((int) Math.factorial(i));
            } else {
                int sum = 0;
                for (int j = 1; j <= i; j++) {
                    sum += j;
                }
                result.add(sum);
            }
        }
        return result;
    }
}

