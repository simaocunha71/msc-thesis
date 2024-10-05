        int n = grid.size();
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res.add(grid.get(i).get(j));
            }
        }
        Collections.sort(res);
        return res.subList(0, k);
    }
}

