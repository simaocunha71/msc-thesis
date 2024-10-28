        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int temp = 1;
            if (i % 2 == 0) {
                for (int j = 2; j <= i; j++) {
                    temp *= j;
                }
            } else {
                for (int j = 1; j <= i; j++) {
                    temp += j;
                }
            }
            result.add(temp);
        }
        return result;
    }
}

