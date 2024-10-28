```java
const simplify = (x, n) => {
  let t = x.split('/');
  let u = n.split('/');
  let a = Number(t[0]);
  let b = Number(t[1]);
  let c = Number(u[0]);
  let d = Number(u[1]);
  if (a * d % b * c === 0) {
    return true;
  }
  return false;
}
```
