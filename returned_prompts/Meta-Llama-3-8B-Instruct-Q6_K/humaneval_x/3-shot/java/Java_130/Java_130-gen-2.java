        List<Integer> result = new ArrayList<>();
        result.add(3);
        if (n > 0) {
            result.add(1);
            if (n > 1) {
                result.add(2);
                for (int i = 3; i <= n; i++) {
                    int sum = result.get(i - 1) + result.get(i - 2) + result.get(i - 3);
                    result.add(sum);
                }
            }
        }
        return result.subList(0, n + 1);
    }
}

