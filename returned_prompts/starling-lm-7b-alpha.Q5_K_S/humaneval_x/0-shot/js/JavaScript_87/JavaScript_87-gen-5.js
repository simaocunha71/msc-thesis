
  // Initialize a result array
  let result = [];

  // Iterate through each row in the list
  for (let i = 0; i < lst.length; i++) {
    let row = lst[i];

    // Iterate through each element in the row
    for (let j = 0; j < row.length; j++) {
      let element = row[j];

      // If the element is equal to x, add the row index and column index to the result array
      if (element === x) {
        result.push([i, j]);
      }
    }
  }

  // Sort the result array by row index in ascending order, and then by column index in descending order using sort() method
  result.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

  return result;
};






// Test cases:
console.log(getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)); // [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

console.log(getRow([], 1)); // []

console.log(getRow([[], [1], [1, 2, 3]], 3)); // [(2, 2)]

console.log(getRow([
  [1, 2],
  [3, 4, 5],
  [6, 7, 8, 9]
], 7)); // [(2, 2)]

console.log(getRow([
  [1, 2, 3],
  [4, 5],
  [6, 7, 8, 9]
], 9)); // [(2, 3)]

console.log(getRow([
  [1, 2, 3],
  [4, 5],
  [6, 7, 8, 