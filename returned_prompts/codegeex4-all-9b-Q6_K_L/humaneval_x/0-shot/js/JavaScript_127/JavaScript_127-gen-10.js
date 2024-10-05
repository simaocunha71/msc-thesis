```java
const intersection = (interval1, interval2) => {
  if (interval1[0] > interval2[1] || interval1[1] < interval2[0]) {
    return "NO";
  }
  const intersectionLength = Math.min(interval1[1], interval2[1]) - Math.max(interval1[0], interval2[0]) + 1;
  if (intersectionLength < 2) {
    return "NO";
  }
  for (let i = 2; i <= Math.sqrt(intersectionLength); i++) {
    if (intersectionLength % i === 0) {
      return "NO";
    }
  }
  return "YES";
}
```
