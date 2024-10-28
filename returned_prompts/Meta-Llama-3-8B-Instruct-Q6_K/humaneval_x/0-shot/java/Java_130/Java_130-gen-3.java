    public List<Integer> tri(int n) {
        List<Integer> result = new ArrayList<>();
        if (n == 0) {
            return result;
        }
        result.add(1);
        if (n == 1) {
            result.add(3);
            return result;
        }
        result.add(3);
        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                int sum = 0;
                for (int j = 1; j <= 3; j++) {
                    sum += result.get(i - j);
                }
                result.add(sum);
            }
        }
        return result;
    }