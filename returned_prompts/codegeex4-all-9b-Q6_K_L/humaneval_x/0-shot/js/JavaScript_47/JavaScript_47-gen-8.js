```java
const median = (l) => {
  var sorted = l.slice().sort((a, b) => a - b);
  var len = sorted.length;
  if (len % 2 == 1) return sorted[(len - 1) / 2];
  else return (sorted[(len / 2) - 1] + sorted[len / 2]) / 2.0;
}
```