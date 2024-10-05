        int n = grid.size();
        List<Integer> result = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] == b[2] ? a[0] == b[0] ? a[1] - b[1] : a[0] - b[0] : a[2] - b[2]);
        boolean[][] visited = new boolean[n][n];
        int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        pq.offer(new int[]{0, 0, grid.get(0).get(0)});
        for (int i = 0; i < k; i++) {
            int[] current = pq.poll();
            result.add(current[2]);
            for (int[] dir : directions) {
                int x = current[0] + dir[0], y = current[1] + dir[1];
                if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
                    pq.offer(new int[]{x, y, grid.get(x).get(y)});
                    visited[x][y] = true;
                }
            }
        }
        return result;
    }
}

