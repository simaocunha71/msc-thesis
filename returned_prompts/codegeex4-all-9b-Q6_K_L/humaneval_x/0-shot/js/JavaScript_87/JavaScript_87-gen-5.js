```java
const getRow = (lst, x) => {
  let ar = []
  for (let i = 0; i < lst.length; i++) {
    for (let j = lst[i].length - 1; j >= 0; j--) {
      if (lst[i][j] === x) {
        ar.push([i, j])
      }
    }
  }
  return ar
}
```
