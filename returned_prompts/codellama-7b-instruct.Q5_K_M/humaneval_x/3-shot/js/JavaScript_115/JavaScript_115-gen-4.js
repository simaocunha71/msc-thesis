  var n = grid.length;
  var m = grid[0].length;

  var left = new Array(n).fill(0);
  var right = new Array(n).fill(0);

  for (var i = 0; i < n; i++) {
    for (var j = 0; j < m; j++) {
      if (grid[i][j] == 1) {
        left[i] = j;
      }
    }
  }

  for (var i = n - 1; i >= 0; i--) {
    for (var j = 0; j < m; j++) {
      if (grid[i][j] == 1) {
        right[i] = j;
      }
    }
  }

  var result = 0;
  for (var i = 0; i < n; i++) {
    result += (right[i] - left[i]) + 1;
  }

  return result;
}



