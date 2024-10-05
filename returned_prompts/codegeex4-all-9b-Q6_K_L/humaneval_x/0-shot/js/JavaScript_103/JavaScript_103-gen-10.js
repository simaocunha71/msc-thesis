```java
const roundedAvg = (n, m) => {
  if (n > m) {
    return -1;
  }

  let total = 0;
  let count = 0;
  for (let i = n; i <= m; i++) {
    total += i;
    count++;
  }

  let avg = Math.round(total / count);
  return "0b" + avg.toString(2);
}
```
