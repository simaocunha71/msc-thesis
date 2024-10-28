        int n = grid.size();
        List<Integer> result = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] != b[2] ? a[2] - b[2] : a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        boolean[][] visited = new boolean[n][n];
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        pq.offer(new int[]{0, 0, grid.get(0).get(0)});

        while (result.size() < k) {
            int[] cur = pq.poll();
            if (result.size() > 0 && result.get(result.size() - 1) == cur[2]) continue;
            result.add(cur[2]);
            for (int[] d : dirs) {
                int x = cur[0] + d[0], y = cur[1] + d[1];
                if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
                    visited[x][y] = true;
                    pq.offer(new int[]{x, y, grid.get(x).get(y)});
                }
            }
        }
        return result;
    }
}

