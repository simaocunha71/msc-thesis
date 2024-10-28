        List<Integer> result = new ArrayList<>();
        result.add(3);
        if (n > 1) {
            result.add(1);
            if (n > 2) {
                result.add(3);
                for (int i = 3; i <= n; i++) {
                    int sum = 0;
                    for (int j = 1; j <= i - 1; j++) {
                        sum += result.get(j);
                    }
                    result.add(sum);
                }
            }
        }
        return result;
    }
}