        int N = grid.size();
        boolean[][] visited = new boolean[N][N];
        List<Integer> result = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> grid.get(a[0]).get(a[1]) - grid.get(b[0]).get(b[1]));

        pq.offer(new int[]{0, 0, grid.get(0).get(0)});

        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        while (result.size() < k) {
            int[] cur = pq.poll();
            result.add(grid.get(cur[0]).get(cur[1]));

            for (int[] d : dirs) {
                int x = cur[0] + d[0], y = cur[1] + d[1];
                if (x >= 0 && x < N && y >= 0 && y < N && !visited[x][y]) {
                    visited[x][y] = true;
                    pq.offer(new int[]{x, y, grid.get(x).get(y)});
                }
            }
        }
        return result;
    }
}

