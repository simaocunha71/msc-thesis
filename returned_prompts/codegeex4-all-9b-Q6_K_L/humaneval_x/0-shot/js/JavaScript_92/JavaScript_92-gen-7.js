```java
const anyInt = (x, y, z) => {
  if (x % 1 === 0 && y % 1 === 0 && z % 1 === 0) {
    if ((x + y === z) || (x + z === y) || (y + z === x)) {
      return true
    }
  }
  return false
}
```
