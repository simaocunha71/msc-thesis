  let n = grid.length;
  let result = [];
  let start = 0;
  let path = [grid[0][0]];
  let visited = new Set();
  let queue = [[0, 0, path]];
  visited.add(JSON.stringify([0, 0]));

  while (queue.length > 0) {
    let [x, y, path] = queue.shift();
    if (path.length == k) {
      return path;
    }

    for (let dx = -1; dx <= 1; dx++) {
      for (let dy = -1; dy <= 1; dy++) {
        let nx = x + dx;
        let ny = y + dy;
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited.has(JSON.stringify([nx, ny]))) {
          visited.add(JSON.stringify([nx, ny]));
          let new_path = path.concat([grid[nx][ny]]);
          queue.push([nx, ny, new_path]);
        }
      }
    }
  }
  return [];
}
// Test
console.log(minPath([[1,2,3], [4,5,6], [7,8,9]], 3)); // Output: [1, 2, 1]
console.log(minPath([[5,9,3], [4,1,6], [7,8,2]], 1)); // Output: [1]
console.log(minPath([[1,2,3], [4,5,6], [7,8,9]], 4)); // Output: [1, 2, 3, 1]
console.log(minPath([[5,9,3], [4,1,6], [7,8,2]], 2)); // Output: [1, 6]
console.log(minPath([[1,2,3], [4,5,6], [7,8,9]], 5)); // Output: [1, 2, 3, 1, 2]