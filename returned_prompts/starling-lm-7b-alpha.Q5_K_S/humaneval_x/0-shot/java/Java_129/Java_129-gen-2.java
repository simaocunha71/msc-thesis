        int n = grid.size();
        int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        Queue<int[]> queue = new LinkedList<>();
        Set<Integer> set = new HashSet<>();
        queue.offer(new int[]{0, 0});
        set.add(grid[0][0]);
        List<Integer> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            if (set.size() == k) {
                result = new ArrayList<>(set);
                break A;
            }
            for (int[] d : dir) {
                int x = curr[0] + d[0];
                int y = curr[1] + d[1];
                if (x < 0 || y < 0 || x >= n || y >= n) {
                    continue;
                }
                int currVal = grid[curr[0]][curr[1]];
                int nextVal = grid[x][y];
                if (set.contains(nextVal)) {
                    continue;
                }
                result.add(currVal);
                queue.offer(new int[]{x, y});
                set.add(nextVal);
            }
        }
        return result;
    }
}

















































































































































































