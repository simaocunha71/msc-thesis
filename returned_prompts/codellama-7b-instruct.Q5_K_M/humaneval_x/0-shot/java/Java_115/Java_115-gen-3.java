        int rows = grid.size();
        int cols = grid.get(0).size();

        // DP
        int[][] dp = new int[rows][cols];

        // init
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dp[i][j] = grid.get(i).get(j);
            }
        }

        // BFS
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dp[i][j] == 1) {
                    queue.offer(new int[] { i, j });
                }
            }
        }

        int times = 0;

        while (queue.size() > 0) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int[] current = queue.poll();
                int row = current[0];
                int col = current[1];

                // left
                if (col - 1 >= 0 && dp[row][col - 1] == 1) {
                    dp[row][col - 1] = 0;
                    queue.offer(new int[] { row, col - 1 });
                }

                // right
                if (col + 1 < cols && dp[row][col + 1] == 1) {
                    dp[row][col + 1] = 0;
                    queue.offer(new int[] { row, col + 1 });
                }

                // up
                if (row - 1 >= 0 && dp[row - 1][col] == 1) {
                    dp[row - 1][col] = 0;
                    queue.offer(new int[] { row - 1, col });
                }

                // down
                if (row + 1 < rows && dp[