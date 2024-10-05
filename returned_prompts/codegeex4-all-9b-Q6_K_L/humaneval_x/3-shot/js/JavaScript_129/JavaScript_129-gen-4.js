  var result = [];
  var directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  var visited = {};
  var queue = [];
  var min_value = Infinity;
  var min_path = [];

  for (var i = 0; i < grid.length; i++) {
    for (var j = 0; j < grid[0].length; j++) {
      queue.push([i, j, 0, grid[i][j]]);
    }
  }

  while (queue.length > 0) {
    var current = queue.shift();
    var x = current[0];
    var y = current[1];
    var distance = current[2];
    var value = current[3];

    if (distance == k) {
      if (value < min_value) {
        min_value = value;
        min_path = [value];
      } else if (value == min_value) {
        min_path.push(value);
      }
    } else {
      for (var d of directions) {
        var nx = x + d[0];
        var ny = y + d[1];
        if (nx >= 0 && nx < grid.length && ny >= 0 && ny < grid[0].length && !visited[nx + ',' + ny]) {
          visited[nx + ',' + ny] = true;
          queue.push([nx, ny, distance + 1, value]);
        }
      }
    }
  }

  return min_path;
}