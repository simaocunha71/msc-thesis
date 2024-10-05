        List<Integer> result = new ArrayList<>();
        int current = n;
        result.add(current);
        for (int i = 0; i < n - 1; i++) {
            current += 2;
            result.add(current);
        }
        return result;
    }
}

