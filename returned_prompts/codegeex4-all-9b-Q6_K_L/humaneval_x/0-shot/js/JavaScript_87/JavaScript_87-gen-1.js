```
const getRow = (lst, x) => {
  let arr = []
  for (let i = 0; i < lst.length; i++) {
    for (let j = lst[i].length - 1; j > -1; j--) {
      if (lst[i][j] === x) {
        arr.push([i, j])
      }
    }
  }
  return arr
}
```