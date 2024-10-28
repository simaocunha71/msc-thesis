  let result = [];

  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) {
        result.push([i, j]);
      }
    }
  }

  result.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });

  return result;
}

console.log(getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)) //== [ [ 0, 0 ], [ 1, 4 ], [ 1, 0 ], [ 2, 5 ], [ 2, 0 ] ]

console.log(getRow([], 1)) //== []

console.log(getRow([[], [1], [1, 2, 3]], 3)) //== [ [ 2, 2 ] ]

The solution is written in JavaScript.
The code initializes an empty list, result. Then it iterates over the given list and if the element in the list matches the given number, it stores the coordinate of the element in the list. Finally, it sorts the list in ascending order by row and in descending order by column before returning the sorted list.
*/

// ----------------------------------------
// SOLUTION 2:
// ----------------------------------------

