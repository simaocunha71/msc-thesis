```java
const anyInt = (x, y, z) => {
  if (Math.floor(x) !== x || Math.floor(y) !== y || Math.floor(z) !== z) {
    return false;
  }
  let sum = x + y + z;
  if (x === sum - x || y === sum - y || z === sum - z) {
    return true;
  }
  return false;
}
```
