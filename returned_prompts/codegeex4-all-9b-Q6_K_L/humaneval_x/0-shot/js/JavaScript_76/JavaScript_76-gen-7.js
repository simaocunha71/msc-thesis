```java
const isSimplePower = (x, n) => {
  let p = 1
  while (p <= x) {
    if (p === x) {
      return true
    }
    p *= n
  }
  return false
}
```
