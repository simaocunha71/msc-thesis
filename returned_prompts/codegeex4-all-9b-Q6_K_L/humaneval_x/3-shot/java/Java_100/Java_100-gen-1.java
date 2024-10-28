        List<Integer> result = new ArrayList<>();
        int current = n;
        for (int i = 0; i < n; i++) {
            result.add(current);
            current += i % 2 == 1 ? 2 : 1;
        }
        return result;
    }
}

