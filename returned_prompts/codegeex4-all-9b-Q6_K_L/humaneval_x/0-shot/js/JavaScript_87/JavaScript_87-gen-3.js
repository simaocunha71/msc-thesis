```js
const getRow = (lst, x) => {
  let res = []
  for (let i = 0; i < lst.length; i++) {
    for (let j = lst[i].length - 1; j >= 0; j--) {
      if (lst[i][j] === x) {
        res.push([i, j])
      }
    }
  }
  return res
}
```
