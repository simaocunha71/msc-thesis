```java
const triplesSumToZero = (l) => {
  for (const i of l) {
    for (const j of l) {
      for (const k of l) {
        if (i + j + k === 0 && i !== j && i !== k && j !== k) {
          return true;
        }
      }
    }
  }
  return false;
}
```
