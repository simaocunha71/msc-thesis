```java
const intersection = (interval1, interval2) => {
  const [start1, end1] = interval1;
  const [start2, end2] = interval2;
  const intersectionStart = Math.max(start1, start2);
  const intersectionEnd = Math.min(end1, end2);
  const intersectionLength = intersectionEnd - intersectionStart + 1;
  if (intersectionLength <= 1) {
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