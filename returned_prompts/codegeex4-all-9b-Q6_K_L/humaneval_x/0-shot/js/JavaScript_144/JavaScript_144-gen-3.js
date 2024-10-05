```java
const simplify = (x, n) => {
  let a = x.split("/")
  let b = n.split("/")
  return (a[0] * b[1] === a[1] * b[0])
}
```
