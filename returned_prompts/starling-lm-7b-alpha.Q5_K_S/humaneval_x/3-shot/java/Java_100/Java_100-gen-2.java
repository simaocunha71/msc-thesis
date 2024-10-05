        List<Integer> result = new ArrayList<>();
        int current = n;
        for (int i = 0; i < n; i++) {
            result.add(current);
            if (current % 2 == 0) {
                current += 1;
            } else {
                current += 2;
            }
        }
        return result;
    }
}

