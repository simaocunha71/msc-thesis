        int N = grid.size();
        List<Integer> result = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] == b[2] ? a[0] == b[0] ? a[1] - b[1] : a[0] - b[0] : a[2] - b[2]);
        boolean[][] visited = new boolean[N][N];
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        pq.offer(new int[]{0, 0, grid.get(0).get(0)});

        while (result.size() < k) {
            int[] cur = pq.poll();
            if (visited[cur[0]][cur[1]]) continue;
            result.add(cur[2]);
            visited[cur[0]][cur[1]] = true;

            for (int[] dir : dirs) {
                int x = cur[0] + dir[0], y = cur[1] + dir[1];
                if (x < 0 || x >= N || y < 0 || y >= N || visited[x][y]) continue;
                pq.offer(new int[]{x, y, grid.get(x).get(y)});
            }
        }

        return result;
    }
}

