```java
const getRow = (lst, x) => {
  let l = []
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] == x) {
        l.push([i, j])
      }
    }
  }
  l.sort((a, b) => {
    if (a[0] == b[0]) {
      return b[1] - a[1]
    }
    return a[0] - b[0]
  })
  return l
}
```