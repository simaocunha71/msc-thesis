  let rows = grid.length;
  let cols = grid[0].length;
  let path = [];
  let minPath = null;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      let currentPath = [];
      let currentRow = i;
      let currentCol = j;
      let currentPathValue = grid[currentRow][currentCol];
      currentPath.push(currentPathValue);

      for (let step = 1; step <= k; step++) {
        let directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        let minDirection = null;
        let minDistance = Infinity;
        for (let direction of directions) {
          let newRow = currentRow + direction[0];
          let newCol = currentCol + direction[1];
          if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
            let newDistance = Math.abs(grid[newRow][newCol] - currentPathValue);
            if (newDistance < minDistance) {
              minDistance = newDistance;
              minDirection = direction;
            }
          }
        }
        currentRow += minDirection[0];
        currentCol += minDirection[1];
        currentPathValue = grid[currentRow][currentCol];
        currentPath.push(currentPathValue);
      }

      let currentPathValueList = currentPath.slice();
      for (let i = 0; i < currentPath.length; i++) {
        currentPathValueList[i] = currentPath[i].toString();
      }
      currentPathValueList.sort((a, b) => a.localeCompare(b));
      let currentPathValueStr = currentPathValueList.join('');

      if (minPath == null || currentPathValueStr < minPath) {
        minPath = currentPathValueStr;
      }
    }
  }

  let minPathList = minPath.split('');
  for (let i = 0; i < minPathList.length; i++) {
    minPathList[i] = parseInt(minPathList[i]);
  }
  return minPathList;
}

// Test cases
console.log(minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3));  // Output: [1, 2,