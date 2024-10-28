    int m = grid.size();
    int n = grid.get(0).size();
    int[][] dp = new int[m][n];

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(grid.get(i).get(j) == 1) {
                dp[i][j] = 1;
            }
        }
    }

    int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}};
    boolean[][] visited = new boolean[m][n];
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(visited[i][j]) continue;

            int count = 0;
            Deque<Integer> q = new ArrayDeque<>();
            q.add(i); q.add(j); visited[i][j] = true;

            while(!q.isEmpty()) {
                int x = q.poll(), y = q.poll();
                count++;
                for(int[] d: dir) {
                    int x1 = x + d[0], y1 = y + d[1];
                    if(x1 < 0 || x1 >= m || y1 < 0 || y1 >= n) continue;
                    if(visited[x1][y1] || grid.get(x1).get(y1) == 0) continue;
                    visited[x1][y1] = true;
                    q.add(x1); q.add(y1);
                }
            }

            dp[i][j] += count;
        }
    }

    int cnt = 0;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(dp[i][j] > capacity) {
                cnt++;
                dp[i][j] -= capacity;
            }
            else {
