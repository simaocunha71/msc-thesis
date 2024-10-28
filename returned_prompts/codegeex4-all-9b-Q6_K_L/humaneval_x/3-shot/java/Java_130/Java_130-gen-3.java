        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);

        if (n == 0) {
            return result;
        }

        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                result.add(result.get(i - 1) + result.get(i - 2) + result.get(i + 1));
            }
        }
        return result;
    }
}

