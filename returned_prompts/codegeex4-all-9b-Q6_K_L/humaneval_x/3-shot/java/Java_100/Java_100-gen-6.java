        List<Integer> result = new ArrayList<>();
        int level = 1;
        for (int i = 0; i < n; i++) {
            result.add(n + level);
            level += 2;
        }
        return result;
    }
}

