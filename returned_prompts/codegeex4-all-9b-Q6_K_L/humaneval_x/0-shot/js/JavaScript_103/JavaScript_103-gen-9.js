```js
const roundedAvg = (n, m) => {
  if (n > m) return -1;
  const sum = (m * (m + 1) - (n - 1) * n) / 2;
  const rounded = Math.round(sum);
  return "0b" + rounded.toString(2);
}
```