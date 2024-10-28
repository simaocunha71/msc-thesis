        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int value = 1;
            if (i % 2 == 0) {
                for (int j = 2; j <= i; j++) {
                    value *= j;
                }
            } else {
                for (int j = 1; j <= i; j++) {
                    value += j;
                }
            }
            result.add(value);
        }
        return result;
    }
}

