        int rows = grid.size();
        int cols = grid.get(0).size();
        int[][] dist = new int[rows][cols];
        int[][] prev = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dist[i][j] = Integer.MAX_VALUE;
                prev[i][j] = -1;
            }
        }
        dist[0][0] = 0;
        prev[0][0] = -1;

        for (int i = 0; i < k; i++) {
            boolean change = false;
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    int[] next = getNext(row, col, rows, cols);
                    for (int[] n : next) {
                        if (n[0] < 0 || n[1] < 0) {
                            continue;
                        }
                        if (dist[n[0]][n[1]] > dist[row][col] + 1) {
                            dist[n[0]][n[1]] = dist[row][col] + 1;
                            prev[n[0]][n[1]] = row * cols + col;
                            change = true;
                        }
                    }
                }
            }
            if (!change) {
                break;
            }
        }

        List<Integer> res = new ArrayList<>();
        int cur = rows * cols - 1;
        while (cur != -1) {
            res.add(grid.get(cur / cols).get(cur % cols));
            cur = prev[cur / cols][cur % cols];
        }
        Collections.reverse(res);
        return res;
    }

    public int[][] getNext(int row, int col, int rows, int cols) {
        int[][] res = new int[3][2];
        res[0][0] = row - 1;
