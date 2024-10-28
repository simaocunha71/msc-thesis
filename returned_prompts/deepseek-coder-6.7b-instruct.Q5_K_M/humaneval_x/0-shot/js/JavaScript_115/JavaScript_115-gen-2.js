  let count = 0;
  let totalWells = 0;
  
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        totalWells++;
        count++;
      }
    }
  }
  
  while (count > 0) {
    count -= capacity;
    totalWells--;
  }
  
  return totalWells;
}

// Tests
console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)); // 6
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)); // 5
console.log(maxFill([[0,0,0], [0,0,0]], 5)); // 0

/*
  Explanation:
  In the first example, we have 3 wells and we can empty them all in 6 steps:
  Empty the bucket (1 unit) from well 1,
  Empty the bucket (1 unit) from well 2,
  Empty the bucket (2 units) from well 3,
  Empty the bucket (1 unit) from well 1,
  Empty the bucket (1 unit) from well 2,
  Empty the bucket (1 unit) from well 3.

  In the second example, we have 4 wells and we can empty them all in 5 steps:
  Empty the bucket (2 units) from well 1,
  Empty the bucket (2 units) from well 2,
  Empty the bucket (1 unit) from well 3,
  Empty the bucket (1 unit) from well 4,
  Empty the bucket (1 unit) from well 3.

  In the third example, we have 2 wells and we can empty them all in 0 steps:
  Empty the bucket