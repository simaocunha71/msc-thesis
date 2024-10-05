```java
const anyInt = (x, y, z) => {
  if (!Number.isInteger(x) || !Number.isInteger(y) || !Number.isInteger(z)) return false;
  let sum = x + y + z;
  if (sum == x || sum == y || sum == z) return true;
  return false;
}
```
