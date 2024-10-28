  let result = [];
  let minPath = [];
  let visited = new Set();
  let queue = [[grid[0][0], 0, 0]];
  visited.add(grid[0][0]);
  while (queue.length > 0) {
    let [cell, pathLen, index] = queue.shift();
    if (pathLen === k) {
      if (minPath.length === 0 || result.sort((a, b) => a - b).join(',') < minPath.sort((a, b) => a - b).join(',')) {
        minPath = result;
      }
    }
    for (let i = -1; i <= 1; i++) {
      for (let j = -1; j <= 1; j++) {
        if (i === 0 && j === 0) {
          continue;
        }
        let newRow = Math.max(0, index + i);
        let newCol = Math.max(0, Math.min(grid[0].length - 1, index + j));
        let newCell = grid[newRow][newCol];
        if (!visited.has(newCell)) {
          visited.add(newCell);
          result.push(newCell);
          queue.push([newCell, pathLen + 1, newRow * grid[0].length + newCol]);
          result.pop();
        }
      }
    }
  }
  return minPath;
}
// let grid = [[1,2,3], [4,5,6], [7,8,9]];
// let k = 3;
// console.log(minPath(grid, k)); // Output: [1, 2, 1]
// let grid = [[5,9,3], [4,1,6], [7,8,2]];
// let k = 1;
// console.log(minPath(grid, k)); // Output: [1]