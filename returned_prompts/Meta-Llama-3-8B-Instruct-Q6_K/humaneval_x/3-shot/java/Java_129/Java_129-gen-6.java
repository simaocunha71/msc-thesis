        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            for (List<Integer> row : grid) {
                result.add(row.get(0));
                grid.get(0).remove(0);
            }
        }
        return result;
    }
}

