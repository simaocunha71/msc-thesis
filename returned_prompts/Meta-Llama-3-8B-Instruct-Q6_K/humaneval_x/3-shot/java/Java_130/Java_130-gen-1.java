        List<Integer> result = new ArrayList<>();
        result.add(3);
        if (n > 0) {
            result.add(1);
            if (n > 1) {
                result.add(1);
                for (int i = 3; i <= n; i++) {
                    result.add(result.get(i - 1) + result.get(i - 2) + (i % 2 == 0 ? 1 : result.get(i - 3)));
                }
            }
        }
        return result;
    }
}

