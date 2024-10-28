  let coords = [];

  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) {
        coords.push([i, j]);
      }
    }
  }

  coords.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });

  return coords;
}

console.log(getRow([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 1))
  
console.log(getRow([], 1))

console.log(getRow([[], [1], [1, 2, 3]], 3))
  
  
  
/*
  The function works by iterating over each element in the 2D array
  and checking if it matches the target x. If it does, it adds the 
  coordinates (row, column) to the coords array. 

  It then sorts the coords array first by row in ascending order, 
  then by column in descending order.

  Finally, it returns the sorted coordinates array.
*/

// time complexity - O(m*n) where m is the number of rows and n is the number of columns in the 2D list.
// space complexity - O(k) where k is the number of occurrences of x in the 2D list.

// This code is written in JavaScript.

// The problem is about finding and sorting coordinates of a number in a 2D list.
// The approach is to iterate over the 2D list and find the coordinates of the number,
// then sort the coordinates first by rows in ascending order and then by columns in descending order.
// The sort function is used to sort the coordinates.
// The function returns the sorted coordinates.
