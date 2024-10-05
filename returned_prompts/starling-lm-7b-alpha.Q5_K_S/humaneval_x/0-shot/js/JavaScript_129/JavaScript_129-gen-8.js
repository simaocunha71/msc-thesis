    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (i > 0 && j > 0) {
                if (grid[i][j] > grid[i-1][j] && grid[i][j] > grid[i][j-1]) {
                    continue A;
                }
            }
            if (i < grid.length - 1 && j > 0) {
                if (grid[i][j] > grid[i+1][j] && grid[i][j] > grid[i][j-1]) {
                    continue A;
                }
            }
            if (i > 0 && j < grid[i].length - 1) {
                if (grid[i][j] > grid[i-1][j] && grid[i][j] > grid[i][j+1]) {
                    continue A;
                }
            }
            if (i < grid.length - 1 && j < grid[i].length - 1) {
                if (grid[i][j] > grid[i+1][j] && grid[i][j] > grid[i][j+1]) {
                    continue A;
                }
            }
        }
    }
    // return grid[i][j];
    let s = 1;
    let res = [];
    while (s <= k) {
        res.push(grid[i][j]);
        s++;
        if (i > 0 && j > 0) {
            if (grid[i][j] > grid[i-1][j] && grid[i][j] > grid[i][j-1]) {
                i--;
                j--;
            } else if (grid[i][j] > grid[i-1][j] && grid[i][j] > grid[i][j+1]) {
                i--;
                j++;
            } else if (grid[i][j] > grid[i+1][j] && grid[i][j] >