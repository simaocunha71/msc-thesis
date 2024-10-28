    int m = grid.size();
    int n = grid.get(0).size();
    int[][] dp = new int[m][n];
    int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(grid.get(i).get(j) == 0) {
                continue;
            }
            int cnt = grid.get(i).get(j);
            int ans = 0;
            while(cnt > 0) {
                int[] next = {i, j};
                if(cnt < capacity) {
                    next[0] += dirs[ans][0];
                    next[1] += dirs[ans][1];
                    if(next[0] < 0 || next[1] < 0 || next[0] >= m || next[1] >= n) {
                        ans = (ans + 1) % 4;
                        continue;
                    }
                    if(grid.get(next[0]).get(next[1]) == 0) {
                        ans = (ans + 1) % 4;
                        continue;
                    }
                }
                next[0] += dirs[ans][0] * capacity;
                next[1] += dirs[ans][1] * capacity;
                if(next[0] < 0 || next[1] < 0 || next[0] >= m || next[1] >= n) {
                    ans = (ans + 1) % 4;
                    continue;
                }
                if(grid.get(next[0]).get(next[1]) == 0) {
                    ans = (ans + 1) % 4;
                    continue;
                }
                cnt -= capacity;
                dp[next[0]][next[1]] = 1;
                grid.get(next[0]).set(next[1