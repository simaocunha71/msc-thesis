        int N = grid.size();
        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dist[i][j] = grid.get(i).get(j);
            }
        }

        int[][] dirs = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

        int[][] queue = new int[N * N][2];
        int[][] previous = new int[N][N];
        int[][] dist_to_previous = new int[N][N];

        queue[0][0] = 0;
        queue[0][1] = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                previous[i][j] = -1;
                dist_to_previous[i][j] = Integer.MAX_VALUE;
            }
        }
        int head = 0;
        int tail = 1;
        while (head < tail) {
            int current_x = queue[head][0];
            int current_y = queue[head][1];
            head += 1;

            for (int[] dir : dirs) {
                int new_x = current_x + dir[0];
                int new_y = current_y + dir[1];
                if (new_x >= 0 && new_x < N && new_y >= 0 && new_y < N && previous[new_x][new_y] == -1
                        && dist_to_previous[current_x][current_y] + 1 < dist[new_x][new_y]) {
                    previous[new_x][new_y] = current_x;
                    dist_to_previous[new_x][new_y] = dist[new_x][new_y];

                    queue[tail][0] = new_x;
                   