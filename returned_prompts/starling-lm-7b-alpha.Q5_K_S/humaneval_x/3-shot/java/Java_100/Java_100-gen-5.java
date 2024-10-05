        List<Integer> result = new ArrayList<>();
        result.add(n);
        if (n % 2 == 0) {
            for (int i = 2; i <= n; i += 2) {
                result.add(i);
            }
        } else {
            for (int i = 2; i <= n; i += 2) {
                result.add(i);
            }
            result.add(n + 1);
        }
        return result;
    }
}

