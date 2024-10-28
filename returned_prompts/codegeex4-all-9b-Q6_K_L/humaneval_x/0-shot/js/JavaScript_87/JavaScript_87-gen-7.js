```js
const getRow = (lst, x) => {
  let indexes = [];
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) indexes.push([i, j]);
    }
  }
  indexes.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
  return indexes;
}
```