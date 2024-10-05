        List<Integer> result = new ArrayList<>();
        if (n < 0) return result;
        if (n >= 0) result.add(3);
        if (n >= 1) result.add(2);
        if (n >= 2) result.add(8);

        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                result.add(result.get(i - 1) + result.get(i - 2) + result.get(i + 1));
            }
        }
        return result;
    }
}

