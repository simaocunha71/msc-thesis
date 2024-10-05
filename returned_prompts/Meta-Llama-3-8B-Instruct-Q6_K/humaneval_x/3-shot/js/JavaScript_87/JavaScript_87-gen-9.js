  let result = [];
  for (let i = 0; i < lst.length; i++) {
    for (let j = lst[i].length - 1; j >= 0; j--) {
      if (lst[i][j] === x) {
        result.push([i, j]);
      }
    }
  }
  return result.sort((a, b) => a[0] - b[0]).sort((a, b) => b[1] - a[1]);
}