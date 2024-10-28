  var result = [];
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] == x) {
        result.push([i, j]);
      }
    }
  }
  result.sort((a, b) => a[0] - b[0]);
  for (let i = 0; i < result.length; i++) {
    result[i][1] = lst[result[i][0]].length - 1 - result[i][1];
  }
  return result;
}

