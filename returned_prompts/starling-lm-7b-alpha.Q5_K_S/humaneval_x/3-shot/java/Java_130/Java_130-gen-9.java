        List<Integer> result = new ArrayList<>();
        if (n == 0) return result;
        result.add(3);
        if (n == 1) return result;
        result.add(1);
        if (n == 2) return result;
        result.add(2);
        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(1);
            } else {
                result.add(result.get(result.size() - 1) + result.get(result.size() - 2) + result.get(result.size() - 3));
            }
        }
        return result;
    }
}

