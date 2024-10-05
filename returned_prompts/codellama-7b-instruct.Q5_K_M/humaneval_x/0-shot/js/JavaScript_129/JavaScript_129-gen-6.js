  let visited = new Array(grid.length).fill(0).map(a => new Array(grid[0].length).fill(0));
  let path = [];
  let queue = [[0, 0]];

  while(queue.length > 0) {
    let node = queue.shift();
    if(visited[node[0]][node[1]] === 1) continue;
    visited[node[0]][node[1]] = 1;
    path.push(grid[node[0]][node[1]]);
    if(path.length >= k) return path;
    //up
    if(node[0] - 1 >= 0 && visited[node[0] - 1][node[1]] !== 1) queue.push([node[0] - 1, node[1]]);
    //right
    if(node[1] + 1 < grid[0].length && visited[node[0]][node[1] + 1] !== 1) queue.push([node[0], node[1] + 1]);
    //down
    if(node[0] + 1 < grid.length && visited[node[0] + 1][node[1]] !== 1) queue.push([node[0] + 1, node[1]]);
    //left
    if(node[1] - 1 >= 0 && visited[node[0]][node[1] - 1] !== 1) queue.push([node[0], node[1] - 1]);
  }
  return path;
}

