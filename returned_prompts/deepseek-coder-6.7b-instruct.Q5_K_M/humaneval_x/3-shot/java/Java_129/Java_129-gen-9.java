        int n = grid.size();
        int[][] dist = new int[n][n];
        for (int[] row: dist)
            Arrays.fill(row, Integer.MAX_VALUE);
        int[][] moves = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        heap.offer(new int[]{0, 0, grid.get(0).get(0)});
        dist[0][0] = grid.get(0).get(0);
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            if (cur[2] > dist[cur[0]][cur[1]]) continue;
            for (int[] move: moves) {
                int nr = cur[0] + move[0], nc = cur[1] + move[1];
                if (nr < 0 || nc < 0 || nr >= n || nc >= n) continue;
                if (dist[nr][nc] > dist[cur[0]][cur[1]] + grid.get(nr).get(nc)) {
                    dist[nr][nc] = dist[cur[0]][cur[1]] + grid.get(nr).get(nc);
                    heap.offer(new int[]{nr, nc, dist[nr][nc]});
                }
            }
        }
        List<Integer> path = new ArrayList<>();
        int r = n - 1, c = n - 1;
        while (true) {
            path.add(grid.get(r).get(c));
            if (r == 0 && c == 0) break;
            for (int[] move: moves) {
                int pr = r + move[0], pc = c + move[1];
                if (pr < 0 || pc < 0 || pr >= n || pc >= n) continue;
                if (dist[pr][pc] + grid.get(r).get(c) == dist[r][c