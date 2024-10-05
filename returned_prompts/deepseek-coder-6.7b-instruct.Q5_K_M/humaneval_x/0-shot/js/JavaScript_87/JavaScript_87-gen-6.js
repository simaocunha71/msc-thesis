  let res = [];
  
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) {
        res.push([i, j]);
      }
    }
  }

  res.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

  return res;
}

console.log(getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)); //== [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

console.log(getRow([], 1)); //== []

console.log(getRow([[], [1], [1, 2, 3]], 3)); //== [(2, 2)]

This solution iterates over each row and each column in the given 2D list, checking if the current element matches x. If a match is found, it adds a tuple (row, column) to the result list. The result list is then sorted first by the row index in ascending order, and then by the column index in descending order.
*/

module.exports = getRow;
