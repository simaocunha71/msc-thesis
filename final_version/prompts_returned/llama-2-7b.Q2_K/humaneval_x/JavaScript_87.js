/*
  You are given a 2 dimensional data, as a nested lists,
  which is similar to matrix, however, unlike matrices,
  each row may contain a different number of columns.
  Given lst, and integer x, find integers x in the list,
  and return list of tuples, [(x1, y1), (x2, y2) ...] such that
  each tuple is a coordinate - (row, columns), starting with 0.
  Sort coordinates initially by rows in ascending order.
  Also, sort coordinates of the row by columns in descending order.
  
  Examples:
  getRow([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
  getRow([], 1) == []
  getRow([[], [1], [1, 2, 3]], 3) == [(2, 2)]
  */
const getRow = (lst, x) => {
  const ans = [];
  for (let i = lst.length - 1; i > -1; i--) {
    if (!ans[i])
      ans[i] = [];

    for (let j = lst[i].length - 1; j > -1; j--) {
      let y = 0;
      if (lst[i][j] != null && x == parseInt(lst[i][j])) {
        ans.push([i, j]);
        break;
      } else {
        for (let z = i - 1; z > -1; z--) {
          if (!ans[z])
            continue;
          let y2 = parseInt(lst[z][j] || '');
          ans[i + j].push([z, y]);
          break;
        }
      }
    }
  }
  return ans;
};
