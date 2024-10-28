        List<Integer> result = new ArrayList<>();
        if (n == 0) return result;
        result.add(3);
        if (n == 1) return result;
        result.add(1);
        result.add(2);
        if (n == 2) return result;

        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                result.add(result.get(result.size() - 1) + result.get(result.size() - 2) + result.get(result.size() - 3) + 1);
            }
        }
        return result;
    }
}

