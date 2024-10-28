```java
const isSimplePower = (x, n) => {
  let p = 1
  while (p < x) {
    p *= n
  }
  return p === x
}
```
