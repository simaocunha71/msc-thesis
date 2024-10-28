        int n = grid.size();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] != b[2] ? a[2] - b[2] : a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        boolean[][] visited = new boolean[n][n];
        pq.offer(new int[]{0, 0, grid.get(0).get(0)});
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        List<Integer> res = new ArrayList<>();

        while (res.size() < k) {
            int[] cur = pq.poll();
            if (visited[cur[0]][cur[1]]) continue;
            visited[cur[0]][cur[1]] = true;
            res.add(cur[2]);
            for (int[] d : dirs) {
                int x = cur[0] + d[0], y = cur[1] + d[1];
                if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
                    pq.offer(new int[]{x, y, grid.get(x).get(y)});
                }
            }
        }

        return res;
    }
}

