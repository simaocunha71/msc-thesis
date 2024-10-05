```java
const stringSequence = (n) => {
  let sequence = '';
  for (let i = 0; i <= n; i++) {
    sequence += i + ' ';
  }
  return sequence.trim();
}
```