
let result = [];

lst.forEach((row, i) => {
  if (row && row.includes(x)) {
    result.push([i, row.lastIndexOf(x)]);
  }
});

result.sort((a, b) => a[0] - b[0]);
result.forEach((item) => {
  item[1] = item[1].reverse();
});

return result;
};

getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1); // == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
getRow([], 1) == []; // == []
getRow([[], [1], [1, 2, 3]], 3) == [(2, 2)]; // == [(2, 2)]



*/

A: Here's my solution for the problem:

```javascript
const getRow = (lst, x) => {
  let result = [];
  lst.forEach((row, i) => {
    if (row && row.includes(x)) {
      result.push([i, row.lastIndexOf(x)]);
    }
  });
  result.sort((a, b) => a[0] - b[0]);
  result.forEach((item) => {
    item[1] = item[1].reverse();
  });
  return result;
};
```

This function `getRow` takes in a 2-dimensional nested list `lst` and an integer `x`. It initializes an empty array `result` to store the coordinates of the occurrence of `x` in `lst`. 

The function then iterates over each `row` in `lst`. If the `row` is present and contains the `x`, it pushes a tuple `[i, row.lastIndexOf(x)]` to the `result` array. Here, `i` represents the index of the row in `lst`, and `row