        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                result.add(i);
            } else {
                result.add(i + 1);
            }
        }
        return result;
    }
}

