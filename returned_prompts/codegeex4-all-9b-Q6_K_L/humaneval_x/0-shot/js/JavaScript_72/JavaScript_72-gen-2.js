```java
const willItFly = (q, w) => {
  if (q.reduce((prev, item) => prev + item, 0) > w) {
    return false;
  }
  return q.join('') == q.reverse().join('');
}
```
