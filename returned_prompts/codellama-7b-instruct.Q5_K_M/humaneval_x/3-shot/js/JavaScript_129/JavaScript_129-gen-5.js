  const m = grid.length;
  const n = grid[0].length;
  let visited = new Array(m).fill(0).map(x => new Array(n).fill(0));

  let result = [];
  let current = [0, 0];

  let queue = [[current, 0]];

  while (queue.length > 0) {
    let [node, level] = queue.shift();
    if (visited[node[0]][node[1]]) continue;
    visited[node[0]][node[1]] = true;
    if (level == k) result.push(grid[node[0]][node[1]]);
    else {
      let neighbors = [
        [node[0] - 1, node[1]],
        [node[0] + 1, node[1]],
        [node[0], node[1] - 1],
        [node[0], node[1] + 1],
      ].filter(x => 0 <= x[0] < m && 0 <= x[1] < n);
      for (let neighbor of neighbors) {
        queue.push([neighbor, level + 1]);
      }
    }
  }

  return result;
}



