    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid.length; j++) {
            if (grid[i][j] === 1) {
                let path = [];
                path.push(grid[i][j]);
                if (i > 0) {
                    path.push(grid[i - 1][j]);
                }
                if (j > 0) {
                    path.push(grid[i][j - 1]);
                }
                if (path.length === k) {
                    return path;
                }
                if (i < grid.length - 1 && grid[i + 1][j] < grid[i][j] + 1) {
                    path.push(grid[i + 1][j]);
                }
                if (j < grid.length - 1 && grid[i][j + 1] < grid[i][j] + 1) {
                    path.push(grid[i][j + 1]);
                }
                if (path.length === k) {
                    return path;
                }
                continue A;
            }
        }
    }
};





/*
Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
each cell of the grid contains a value. Every integer in the range [1, N * N]
inclusive appears exactly once on the cells of the grid.

You have to find the minimum path of length k in the grid. You can start
from any cell, and in each step you can move to any of the neighbor cells,
in other words, you can go to cells which share an edge with you current
cell.

Please note that a path of length k means visiting exactly k cells (not
necessarily distinct).

A path A (of length k) is considered less than a path B (of length k) if
after making the ordered lists of the values on the cells that A and B go
through (let's call them lst_A and lst_B), lst_