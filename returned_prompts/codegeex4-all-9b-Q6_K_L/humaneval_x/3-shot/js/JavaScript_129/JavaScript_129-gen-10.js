  var result = [];

  var x = 0;
  var y = 0;
  var n = grid.length;

  for (var i = 0; i < k; i++) {
    result.push(grid[x][y]);
    if (x == n - 1 && y == n - 1) {
      break;
    }
    if (y < n - 1) {
      y += 1;
    } else {
      x += 1;
    }
  }

  return result;
}

const grid1 = [ [1,2,3], [4,5,6], [7,8,9]];
const k1 = 3;
const grid2 = [ [5,9,3], [4,1,6], [7,8,2]];
const k2 = 1;

console.log(minPath(grid1, k1));
console.log(minPath(grid2, k2));