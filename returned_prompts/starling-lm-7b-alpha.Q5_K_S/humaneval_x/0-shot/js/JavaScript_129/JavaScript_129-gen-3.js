    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1) {
                grid[i][j] = 0;
                if (i > 0) {
                    grid[i-1][j] -= 1;
                }
                if (i < grid.length-1) {
                    grid[i+1][j] -= 1;
                }
                if (j > 0) {
                    grid[i][j-1] -= 1;
                }
                if (j < grid[i].length-1) {
                    grid[i][j+1] -= 1;
                }
                if (grid[i][j] === 0) {
                    continue A;
                }
                return grid[i][j] + minPath(grid, k-1).slice(1);
            }
        }
    }
    return [grid[grid.length-1][grid[grid.length-1].length-1]];
};

// console.log(minPath([[1,2,3],[4,5,6],[7,8,9]],3));
// console.log(minPath([[5,9,3],[4,1,6],[7,8,2]],1));
// console.log(minPath([[5,9,3],[4,1,6],[7,8,2]],2));
// console.log(minPath([[1,2,3],[4,5,6],[7,8,9]],2));
// console.log(minPath([[1,2,3],[4,5,6],[7,8,9]],4));

/*
Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
each cell of the grid contains a value. Every integer in the range [1, N * N]
inclusive appears exactly once on the cells of the grid.

You have to find the minimum