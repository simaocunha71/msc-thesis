    public List<Integer> tri(int n) {
        List<Integer> result = new ArrayList<>();
        if (n == 0) {
            return result;
        }
        result.add(3);
        if (n == 1) {
            return result;
        }
        result.add(1);
        if (n == 2) {
            return result;
        }
        result.add(2);
        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                int a = result.get(i - 1);
                int b = result.get(i - 2);
                int c = result.get(i - 3);
                result.add(a + b + c);
            }
        }
        return result;
    }
