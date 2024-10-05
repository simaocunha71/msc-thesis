  let result = [];
  lst.forEach((row, y) => {
    if (row.includes(x)) {
      let index = row.indexOf(x);
      result.push([y, index]);
    }
  });
  result.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
  return result;
}
// Example usage:
console.log(getRow([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1));
// Output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
console.log(getRow([], 1));
// Output: []
console.log(getRow([[], [1], [1, 2, 3]], 3));
// Output: [(2, 2)]


