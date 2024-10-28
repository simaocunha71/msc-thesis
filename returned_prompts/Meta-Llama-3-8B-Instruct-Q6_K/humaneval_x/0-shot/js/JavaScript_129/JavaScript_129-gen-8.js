```
// Create a hashmap to store the values of the cells in the grid
const valueMap = {};
for (let i = 0; i < grid.length; i++) {
  for (let j = 0; j < grid[i].length; j++) {
    valueMap[grid[i][j]] = true;
  }
}

// Create a hashmap to store the visited cells
const visited = {};

// Create a queue for BFS and add the starting cell to it
const queue = [[0, 0]];
visited[[0, 0]] = true;

// Initialize the result array
let result = [];
let visitedValues = [];

// Perform BFS
while (queue.length > 0) {
  const [row, col] = queue.shift();
  const currentValue = grid[row][col];

  // Add the current value to the result array if it's not visited before
  if (!visitedValues.includes(currentValue)) {
    result.push(currentValue);
    visitedValues.push(currentValue);
  }

  // Add the neighbors to the queue if they are not visited before
  for (let i = -1; i <= 1; i++) {
    for (let j = -1; j <= 1; j++) {
      if (i === 0 && j === 0) continue;
      const newRow = row + i;
      const newCol = col + j;
      if (newRow >= 0 && newRow < grid.length && newCol >= 0 && newCol < grid[0].length && !visited[[newRow, newCol]]) {
        queue.push([newRow, newCol]);
        visited[[newRow, newCol]] = true;
      }
    }
  }

  // If the queue is empty and the length of the result array is k, return the result
  if (queue.length === 0 && result.length === k) return result;
}

// If the length of the result array is less than k, return the result
return result;
```

Explanation:

1. First, we create a hashmap `valueMap` to store the values of the cells in the grid.
2. Then, we create a hashmap `visited` to store the visited cells.
3. We create a queue `queue` and add the starting cell (0, 0) to it.
4. We initialize the result array `result` and the visited values array `visitedValues`.
5. We perform BFS by iterating over the queue