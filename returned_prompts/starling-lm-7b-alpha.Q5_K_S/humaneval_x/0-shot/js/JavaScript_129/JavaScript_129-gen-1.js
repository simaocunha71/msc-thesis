  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        return minpathHelper(grid, i, j, k);
      }
    }
  }
};

const minpathHelper = (grid, i, j, k) => {
  const path = [];
  for (let l = 1; l <= k; l++) {
    const newI = i + (l % 2 === 0 ? 0 : 1);
    const newJ = j + (l % 2 === 0 ? 1 : 0);
    if (newI < 0 || newJ < 0 || newI >= grid.length || newJ >= grid[0].length) {
      return path;
    }
    const cell = grid[newI][newJ];
    path.push(cell);
    grid[newI][newJ] = -1;
  }
  return path;
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
  through (let's call them lst_A and lst_B), lst_A is lexicographically less
  than lst_B, in other words, there exist an integer index i