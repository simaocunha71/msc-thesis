```java
const anyInt = (x, y, z) => {
  if (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) {
    return (x === y + z || y === x + z || z === x + y);
  }
  return false;
}
```
