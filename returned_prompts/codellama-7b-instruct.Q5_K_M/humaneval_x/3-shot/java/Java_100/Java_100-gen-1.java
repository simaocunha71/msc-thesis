        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            result.add(n + 1 - i % 2);
        }
        return result;
    }
}

