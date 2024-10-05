        List<Integer> result = new ArrayList<>();
        result.add(3);
        if (n == 0) {
            return result;
        }
        result.add(1);
        if (n == 1) {
            return result;
        }
        result.add(2);
        if (n == 2) {
            return result;
        }
        for (int i = 3; i <= n; i++) {
            result.add(result.get(i - 1) + result.get(i - 2) + result.get(i - 3));
        }
        return result;
    }
}

