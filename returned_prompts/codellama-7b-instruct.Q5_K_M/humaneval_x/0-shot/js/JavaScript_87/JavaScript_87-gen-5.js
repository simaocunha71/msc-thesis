const getRow = (lst, x) => {
  const xy = [];
  for (let i = 0; i < lst.length; i++) {
    const columns = lst[i].length;
    for (let j = 0; j < columns; j++) {
      if (lst[i][j] === x) {
        xy.push([i, columns - j - 1]);
      }
    }
  }
  return xy.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
};
