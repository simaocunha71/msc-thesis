```js
const largestPrimeFactor = (n) => {
  if (n <= 1) return null;
  if (n === 2) return 2;
  let largest = 1;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    while (n % i === 0) {
      largest = i;
      n = n / i;
    }
  }
  if (n > 1) largest = n;
  return largest;
}
```