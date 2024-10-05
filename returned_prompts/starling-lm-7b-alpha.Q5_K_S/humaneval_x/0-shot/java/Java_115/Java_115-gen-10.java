    int row = grid.size();
    int col = grid.get(0).size();
    int[][] grid1 = new int[row][col];
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            grid1[i][j] = grid.get(i).get(j);
        }
    }
    int[][] grid2 = new int[row][col];
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            grid2[i][j] = grid1[i][j];
        }
    }
    int ans = 0;
    int curr_capacity = 0;
    while(curr_capacity < capacity) {
        int[][] grid3 = new int[row][col];
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                grid3[i][j] = grid2[i][j];
            }
        }
        int[][] grid4 = new int[row][col];
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                int curr = grid3[i][j];
                if(curr == 0) {
                    continue;
                }
                grid4[i][j] = curr - 1;
                if(i + 1 < row) {
                    grid4[i+1][j] += 1;
                }
                if(j + 1 < col) {
                    grid4[i][j+1] += 1;
                }
                if(i + 1 < row && j + 1 < col) {
                    grid4[i+1][j+1] -= 1;
                }
            }
        }
        int[][] grid5 = new int[row][col];
        for(int i = 0; i < row; i