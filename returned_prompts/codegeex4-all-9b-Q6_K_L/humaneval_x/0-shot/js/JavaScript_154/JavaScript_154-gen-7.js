```java
const cycpatternCheck = (a, b) => {
  let n = a.length
  let m = b.length
  if (n < m) return false
  for (let i = 0; i < m; i++) {
    let j = i
    let k = 0
    while (k < m && a[j % n] == b[k]) {
      j++
      k++
    }
    if (k == m) return true
  }
  return false
}
```
