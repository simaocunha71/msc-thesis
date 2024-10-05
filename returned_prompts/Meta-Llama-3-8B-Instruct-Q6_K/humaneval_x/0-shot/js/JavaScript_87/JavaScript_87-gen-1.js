```
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
    } else {
      return a[0] - b[0];
    }
  });
  return result.map(([row, col]) => [row, col]);
};
```


Explanation: 
The function `getRow` takes two parameters: `lst` (a 2D list) and `x` (an integer). It initializes an empty list `result` to store the coordinates of `x` in the list.

It then iterates over each row in the list using a nested loop. For each element in the row, it checks if the element is equal to `x`. If it is, it adds the coordinates of the element to the `result` list.

After finding all the coordinates of `x`, it sorts the `result` list based on the row index (in ascending order) and the column index (in descending order) using the `sort` method.

Finally, it converts the `result` list to a list of tuples (containing row and column indices) using the `map` method and returns the result.