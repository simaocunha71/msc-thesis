        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            result.add(i % 2 == 0 ? i + 1 : i);
        }
        return result;
    }
}

