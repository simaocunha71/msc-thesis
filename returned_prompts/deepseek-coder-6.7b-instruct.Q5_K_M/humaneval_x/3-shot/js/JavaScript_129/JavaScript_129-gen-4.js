  var result 
  var min_path = [...Array(k)].map(e => Infinity)
  var path = [...Array(k)].map(e => Infinity)
  var visited = new Array(grid.length).fill(0).map(() => new Array(grid.length).fill(false))
  var directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  var n = grid.length

  const dfs = (x, y, len) => {
    if (len === k) {
      if (path[k-1] > grid[x][y]) {
        path[k-1] = grid[x][y]
        min_path = [...path]
      }
      return
    }

    if (min_path[len] < grid[x][y]) return
    path[len] = grid[x][y]

    visited[x][y] = true
    for (let i = 0; i < 4; i++) {
      let nx = x + directions[i][0]
      let ny = y + directions[i][1]
      if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
        dfs(nx, ny, len + 1)
      }
    }
    visited[x][y] = false
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j, 0)
    }
  }

  return min_path
}



