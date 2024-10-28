        List<Integer> result = new ArrayList<>();
        if (n == 0) {
            result.add(1);
            return result;
        }
        if (n == 1) {
            result.add(3);
            return result;
        }
        result.add(1);
        result.add(3);
        for (int i = 2; i < n; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                result.add(result.get(i - 1) + result.get(i - 2) + result.get(i - 3));
            }
        }
        return result;
    }
}

