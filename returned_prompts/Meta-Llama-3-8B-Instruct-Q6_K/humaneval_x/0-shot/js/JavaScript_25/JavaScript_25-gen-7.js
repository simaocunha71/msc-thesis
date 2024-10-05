```javascript
const factorize = (n) => {
  let factors = [];
  let i = 2;
  while (i * i <= n) {
    if (n % i) {
      i++;
    } else {
      n /= i;
      factors.push(i);
    }
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
};
```