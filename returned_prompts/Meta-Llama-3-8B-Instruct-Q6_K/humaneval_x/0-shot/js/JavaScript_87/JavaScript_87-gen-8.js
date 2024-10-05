Here is the solution:
```javascript
const getRow = (lst, x) => {
  return lst.reduce((acc, row, i) => {
    row.forEach((element, j) => {
      if (element === x) {
        acc.push([i, j]);
      }
    });
    return acc;
  }, []).sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });
};
```
This function uses the `reduce()` method to iterate over the 2D list and find all occurrences of the target value `x`. It stores the coordinates of these occurrences in an accumulator array `acc`. The `forEach()` method is used to iterate over each row and each element in the row. The coordinates are stored as tuples in the format `[row, column]`. The `sort()` method is used to sort the coordinates first by row (in ascending order) and then by column (in descending order). The `reduce()` method returns the sorted accumulator array. If the target value `x` is not found in the list, the function returns an empty array.