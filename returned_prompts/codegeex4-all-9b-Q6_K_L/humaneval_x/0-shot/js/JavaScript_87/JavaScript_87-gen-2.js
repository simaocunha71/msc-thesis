```js
const getRow = (lst, x) => {
  let coords = []
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) coords.push([i, j])
    }
  }
  coords.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1]
    } else {
      return a[0] - b[0]
    }
  })
  return coords
}
```
