        int n = grid.size();
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> {
            if (a[2] != b[2]) return a[2] - b[2];
            for (int i = 0; i < k; i++) {
                if (a[3 + i] != b[3 + i]) return a[3 + i] - b[3 + i];
            }
            return 0;
        });
        boolean[][] visited = new boolean[n][n];
        queue.offer(new int[]{0, 0, 0, grid.get(0).get(0)});
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (cur[2] == k - 1) {
                List<Integer> path = new ArrayList<>();
                for (int i = 0; i < k; i++) {
                    path.add(cur[3 + i]);
                }
                return path;
            }
            for (int[] dir : directions) {
                int x = cur[0] + dir[0], y = cur[1] + dir[1];
                if (x < 0 || x >= n || y < 0 || y >= n || visited[x][y]) continue;
                visited[x][y] = true;
                int[] next = new int[k + 3];
                System.arraycopy(cur, 0, next, 0, 3);
                next[0] = x;
                next[1] = y;
                next[3 + cur[2] + 1] = grid.get(x).get(y);
                queue.offer(next);
            }
        }
        return null;
    }
}

