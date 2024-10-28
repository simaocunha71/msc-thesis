        int n = grid.size();
        int[][] directions = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[2] != b[2] ? a[2] - b[2] : a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        boolean[][] visited = new boolean[n][n];
        heap.offer(new int[]{0, 0, grid.get(0).get(0)});
        List<Integer> result = new ArrayList<>();

        while (!heap.isEmpty() && result.size() < k) {
            int[] cur = heap.poll();
            int x = cur[0], y = cur[1], val = cur[2];

            if (visited[x][y]) {
                continue;
            }
            visited[x][y] = true;
            result.add(val);

            for (int[] dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                    heap.offer(new int[]{nx, ny, grid.get(nx).get(ny)});
                }
            }
        }
        return result;
    }
}

