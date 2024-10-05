        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    LinkedList<Integer> res = new LinkedList<>();
                    res.add(grid.get(i).get(j));
                    dfs(grid, i, j, k, res);
                    return res;
                }
            }
        }
        return null;
    }

    private void dfs(List<List<Integer>> grid, int i, int j, int k, LinkedList<Integer> res) {
        if (k == 0) return;

        if (i > 0 && grid.get(i - 1).get(j) != 0) {
            res.addFirst(grid.get(i - 1).get(j));
            k--;
        }

        if (i < grid.size() - 1 && grid.get(i + 1).get(j) != 0) {
            res.addFirst(grid.get(i + 1).get(j));
            k--;
        }

        if (j > 0 && grid.get(i).get(j - 1) != 0) {
            res.addFirst(grid.get(i).get(j - 1));
            k--;
        }

        if (j < grid.get(i).size() - 1 && grid.get(i).get(j + 1) != 0) {
            res.addFirst(grid.get(i).get(j + 1));
            k--;
        }

        if (k == 0) return;

        if (i > 0 && grid.get(i - 1).get(j) == 0) {
            grid.get(i - 1).set(j, grid.get(i).get(j) + 1);
            dfs(grid, i - 1, j, k - 1, res);
        }

        if (i < grid.