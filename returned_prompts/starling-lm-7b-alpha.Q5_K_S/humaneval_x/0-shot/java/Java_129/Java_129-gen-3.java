        int n = grid.size();
        int m = grid.get(0).size();
        List<Integer> ans = new ArrayList<>();
        while (k > 0) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (i > 0 && grid.get(i - 1).get(j) < grid.get(i).get(j)) {
                        grid.get(i).set(j, grid.get(i - 1).get(j));
                        continue A;
                    }
                    if (j > 0 && grid.get(i).get(j - 1) < grid.get(i).get(j)) {
                        grid.get(i).set(j, grid.get(i).get(j - 1));
                        continue A;
                    }
                }
            }
            ans.add(grid.get(n - 1).get(m - 1));
            k--;
        }

        Collections.reverse(ans);
        return ans;
    }
}



















    //     List<List<Integer>> grid = new ArrayList<>();
        // grid.add(Arrays.asList(1, 2, 3));
        // grid.add(Arrays.asList(4, 5, 6));
        // grid.add(Arrays.asList(7, 8, 9));
        // System.out.println(minPath(grid, 3));
        // List<List<Integer>> grid = new ArrayList<>();
        // grid.add(Arrays.asList(5, 9, 3));
        // grid.add(Arrays.asList(4, 1, 6));
        // grid.add(Arrays.asList(7, 8, 2));
        // System.out.println(minPath(grid, 1));
        // List<List<Integer>> grid = new ArrayList<>();
        // grid.add(Arrays.asList(1, 2, 3, 4