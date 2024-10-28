```java
const triplesSumToZero = (l) => {
  if (l.length < 3) return false;
  for (let i = 0; i < l.length - 2; i++) {
    for (let j = i + 1; j < l.length - 1; j++) {
      for (let k = j + 1; k < l.length; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
}
```