        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n + 1; i++) {
            if (i == 1) {
                result.add(1);
            } else if (i == 2) {
                result.add(3);
            } else if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                result.add(result.get(i - 2) + result.get(i - 1) + result.get(i + 1));
            }
        }
        return result;
    }
}

