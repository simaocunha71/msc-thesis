        List<Integer> result = new ArrayList<>();
        result.add(n);
        int current = n;

        for (int i = 1; i < n; i++) {
            if (n % 2 == 0) {
                current += 2;
            } else {
                current += 2;
            }
            result.add(current);
        }
        return result;
    }
}

