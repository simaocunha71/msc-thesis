
  const indexes = [];

  lst.forEach((row, i) => {
    row.forEach((elem, j) => {
      if (elem === x) {
        indexes.push([i, j]);
      }
    });
  });

  indexes.sort((a, b) => a[0] - b[0]);
  indexes.forEach((index, i) => {
    indexes[i] = [index[0], index[1] * -1];
  });

  return indexes;
};

console.log(getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1));

console.log(getRow([], 1));

console.log(getRow([[], [1], [1, 2, 3]], 3));


/*
  You are given a 2 dimensional data, as a nested lists,
  which is similar to matrix, however, each row may contain a different number of columns.
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

*/

// Change the variable `x` to test your function