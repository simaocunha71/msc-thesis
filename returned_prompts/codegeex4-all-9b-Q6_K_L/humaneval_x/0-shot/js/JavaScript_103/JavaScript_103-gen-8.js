```javascript
const roundedAvg = (n, m) => {
  if (n > m) return -1;
  let sum = 0;
  for (let i = n; i <= m; i++) {
    sum += i;
  }
  let avg = Math.round(sum / (m - n + 1));
  return "0b" + avg.toString(2);
}
```
