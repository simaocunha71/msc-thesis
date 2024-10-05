```java
const roundedAvg = (n, m) => {
  if (n > m) return -1
  const avg = Math.round((n + m) / 2)
  return '0b' + avg.toString(2)
}
```
