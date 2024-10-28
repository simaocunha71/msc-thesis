Here is the JavaScript code to solve the problem:

```javascript
const getRow = (lst, x) => {
  const result = [];
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
};
```

This code iterates over the list and finds all occurrences of `x`. It then sorts the result based on the row and column indices. The sort function is used to sort the result. If the row indices are the same, the function sorts the column indices in descending order. Otherwise, it sorts the row indices in ascending order. The sorted result is then returned. 

You can test this function with the examples you provided to verify that it returns the expected results. For example:

```javascript
console.log(getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)); // Output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

console.log(getRow([], 1)); // Output: []

console.log(getRow([[], [1], [1, 2, 3]], 3)); // Output: [(2, 2)]
```