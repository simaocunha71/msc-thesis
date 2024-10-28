To solve this problem, we will follow these steps:

1. Initialize an empty list `coordinates` to store the coordinates of the integers `x`.
2. Iterate through each row `i` in the nested list `lst`.
3. For each row, iterate through each element `j` in the row.
4. If `j` is equal to `x`, append the tuple `(i, j)` to the `coordinates` list.
5. Sort the `coordinates` list first by the row index in ascending order and then by the column index in descending order.
6. Finally, return the sorted `coordinates` list.

Here is the updated code:

```javascript
const getRow = (lst, x) => {
  let coordinates = [];
  
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) {
        coordinates.push((i, j));
      }
    }
  }
  
  coordinates.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
  return coordinates;
}
```

Let's test the function with the provided examples:

```javascript
console.log(getRow([
  [1, 2, 3, 4, 5, 6],
  [1, 2, 3, 4, 1, 6],
  [1, 2, 3, 4, 5, 1]
], 1)); // [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

console.log(getRow([], 1)); // []

console.log(getRow([[], [1], [1, 2, 3]], 3)); // [(2, 2)]
```