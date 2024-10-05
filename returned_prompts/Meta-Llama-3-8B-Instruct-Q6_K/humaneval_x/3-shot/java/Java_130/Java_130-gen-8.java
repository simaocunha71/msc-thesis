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
            int sum = result.get(i - 1) + result.get(i - 2) + result.get(i - 3);
            result.add(sum);
        }
        return result;
    }
}