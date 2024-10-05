Here is the solution:

```javascript
const getRow = (lst, x) => {
  return lst.reduce((acc, row, index) => {
    const coords = row.reduce((acc, val, index) => {
      if (val === x) {
        acc.push([index, row.length - 1 - index]);
      }
      return acc;
    }, []);
    return [...acc, ...coords];
  }, []).sort((a, b) => a[0] - b[0] || b[1] - a[1]);
};
```A
This function takes two parameters: lst (the 2D list) and x (the value to be searched). It returns a list of tuples, where each tuple is a coordinate (row, column) where the value x is found.

The function uses the reduce() method to iterate over the 2D list, and for each row, it uses another reduce() method to find the coordinates of x in that row.

The outer reduce() method accumulates the coordinates from each row into an array, and the inner reduce() method finds the coordinates in each row by pushing the coordinates of x into the accumulator array.

Finally, the function sorts the coordinates based on the row and column indices. If two coordinates have the same row index, the one with the larger column index comes first. If two coordinates have the same column index, the one with the smaller row index comes first.

This solution has a time complexity of O(n*m), where n is the number of rows and m is the maximum number of columns in the 2D list, because it needs to iterate over each element in the list once. The space complexity is O(n*m) as well, because it needs to store the coordinates in an array.