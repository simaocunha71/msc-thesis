  /*
  Solution:
    * use a DFS to solve the problem
    * DFS to find the best path to the bottom, and count the number of times 
      the bucket needs to be lowered
  */
  const dfs = (row, col, bucket, water) => {
    // if the current row is the last row, fill the bucket and return
    if (row === grid.length - 1) {
      bucket += water;
      return bucket;
    }

    // if the current cell is a 1, add the water to the bucket and continue
    if (grid[row][col] === 1) {
      bucket += water;
      col++;
      return dfs(row, col, bucket, water);
    }

    // if the current cell is a 0, then the water will need to be lowered
    // to fill the bucket
    bucket += water;
    col++;
    return dfs(row, col, bucket, water - 1);
  }

  // initialize the bucket to 0
  let bucket = 0;

  // start the dfs at the top left corner
  dfs(0, 0, bucket, capacity);

  // return the number of times the bucket needs to be lowered
  return bucket;
}
