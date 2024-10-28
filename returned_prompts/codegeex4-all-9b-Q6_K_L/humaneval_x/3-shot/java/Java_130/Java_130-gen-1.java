        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);

        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(i / 2 + 1);
            } else {
                result.add(result.get(i - 1) + result.get(i - 2) + result.get(i + 1));
            }
        }
        return result;
    }
}

