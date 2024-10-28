        List<Integer> result = new ArrayList<>();
        result.add(3);
        if (n > 0) {
            result.add(1);
            if (n > 1) {
                result.add(1);
                if (n > 2) {
                    for (int i = 3; i <= n; i++) {
                        result.add(result.get(i - 1) + result.get(i - 2) + result.get(i - 3));
                    }
                }
            }
        }
        return result.subList(0, n + 1);
    }
}

