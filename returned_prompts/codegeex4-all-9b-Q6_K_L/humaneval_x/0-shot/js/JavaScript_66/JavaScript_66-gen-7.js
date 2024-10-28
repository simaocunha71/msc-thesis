```java
const digitSum = (s) => {
  return s
    .split('')
    .filter(c => c == c.toUpperCase())
    .reduce((a, b) => a + b.charCodeAt(0), 0);
}
```
