  let result = [];
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] == x) {
        result.push([i, j]);
      }
    }
  }
  result.sort((a, b) => {
    if (a[0] == b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });
  return result;
}



