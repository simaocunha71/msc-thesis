  let coordinates = [];

  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) {
        coordinates.push([i, j]);
      }
    }
  }

  coordinates.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });

  return coordinates;
}

console.log(getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)) // [ [ 0, 0 ], [ 1, 4 ], [ 1, 0 ], [ 2, 5 ], [ 2, 0 ] ]
console.log(getRow([], 1)) // []
console.log(getRow([[], [1], [1, 2, 3]], 3)) // [ [ 2, 2 ] ]


*/

