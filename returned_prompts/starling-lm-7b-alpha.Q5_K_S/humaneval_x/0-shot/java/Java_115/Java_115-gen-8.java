    int n = grid.size();
    int m = grid.get(0).size();
    int[][] gridA = new int[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            gridA[i][j] = grid.get(i).get(j);
        }
    }

    int[][] bucket = new int[n][m];
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    int result = 0;
    Queue<Integer> q = new LinkedList<>();
    Set<Integer> seen = new HashSet<>();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (gridA[i][j] == 1) {
                q.add(i * m + j);
                seen.add(i * m + j);
                result = 1;
                break A;
            }
        }
    }

    while (!q.isEmpty()) {
        int cur = q.poll();
        int i = cur / m;
        int j = cur % m;
        for (int[] dir : dirs) {
            int ni = i + dir[0];
            int nj = j + dir[1];
            if (ni < 0 || ni >= n || nj < 0 || nj >= m || seen.contains(ni * m + nj)) {
                continue;
            }
            if (gridA[ni][nj] == 0) {
                continue;
            }
            if (bucket[ni][nj] + gridA[ni][nj] == capacity) {
                q.add(ni * m + nj);
                seen.add(ni * m + nj);
                continue;
            }
            bucket[ni][nj] += gridA[ni][nj];
            gridA[ni][nj] = 0;
            result++;
        }