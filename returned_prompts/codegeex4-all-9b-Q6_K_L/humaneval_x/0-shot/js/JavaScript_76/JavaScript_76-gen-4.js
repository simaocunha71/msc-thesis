```java
const isSimplePower = (x, n) => {
  if (n === 1) return x === 1;
  let pow = 1;
  while (pow < x) pow *= n;
  return pow === x;
}
```
