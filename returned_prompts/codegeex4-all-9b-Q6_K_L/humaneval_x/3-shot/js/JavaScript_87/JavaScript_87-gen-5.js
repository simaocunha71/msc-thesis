  var result = [];

  for (let row = 0; row < lst.length; row++) {
    for (let col = 0; col < lst[row].length; col++) {
      if (lst[row][col] == x) {
        result.push([row, col]);
      }
    }
  }

  result.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
  return result;
}