        List<Integer> result = new ArrayList<>();
        result.add(3);
        if (n == 0) return result;
        result.add(1);
        if (n == 1) return result;
        result.add(2);
        if (n == 2) return result;
        result.add(4);
        if (n == 3) return result;
        for (int i = 4; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(result.get(result.size() - 3) + 1);
            } else {
                result.add(result.get(result.size() - 4) +
                    result.get(result.size() - 3) + result.get(result.size() - 2));
            }
        }
        return result;
    }
}

