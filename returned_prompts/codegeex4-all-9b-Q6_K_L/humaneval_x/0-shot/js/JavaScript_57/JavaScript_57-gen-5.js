```java
const monotonic = (l) => {
  return l.every((x, i) => i === 0 || x > l[i - 1]) || l.every((x, i) => i === 0 || x < l[i - 1]);
}
```