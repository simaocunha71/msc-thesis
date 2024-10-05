  /*
  Brute force solution:
  We can do the following:
      - Iterate over all possible paths of length k
      - For each possible path, find the minimum value by iterating over all
        the cells and finding the minimum value
      - Return the minimum value found
  The problem is that the number of paths of length k is N^k
  */
  const N = grid.length;
  const paths = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      for (let k = 0; k < N; k++) {
        const path = [];
        const start = { i, j };
        for (let l = 0; l < N; l++) {
          path.push(grid[start.i][start.j]);
          start.i = (start.i + 1) % N;
          if (start.i === 0) {
            start.j = (start.j + 1) % N;
          }
        }
        paths.push(path);
      }
    }
  }
  const minValue = Math.min(...paths.map(path => path.reduce((acc, curr) => acc < curr ? acc : curr, Number.MAX_SAFE_INTEGER)));
  return paths.find(path => path.reduce((acc, curr) => acc < curr ? acc : curr, Number.MAX_SAFE_INTEGER) === minValue);

B:
  /*
  A better solution (but more complex) is to use a dynamic programming
  approach. We can do the following:
      - Build a matrix with N^k rows and N columns
      - In each row, each cell represents a path of length k
      - In each cell, we will store the value of the minimum path that goes
        through this cell
      - For each row, we will store the value of the minimum path that goes
        through the current cell
      - We will iterate over all the rows and for each row we will iterate
        over all the cells
      - If the current cell is the start of a new path (i.e. the path length
        is k