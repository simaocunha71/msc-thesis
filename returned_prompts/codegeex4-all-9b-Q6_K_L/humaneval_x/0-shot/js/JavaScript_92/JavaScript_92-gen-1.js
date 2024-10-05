```java
const anyInt = (x, y, z) => {
  if (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) {
    return (x + y === z || x + z === y || y + z === x)
  }
  return false;
}
```