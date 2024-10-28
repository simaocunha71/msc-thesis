        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                result.add(i + 1);
            } else {
                result.add(i + 3);
            }
        }
        return result;
    }
}

