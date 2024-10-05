```js
const largestPrimeFactor = (n) => {
  let largest = 1;
  while (n % 2 === 0) {
    n /= 2;
    largest = 2;
  }
  let i = 3;
  while (i * i <= n) {
    while (n % i === 0) {
      n /= i;
      largest = i;
    }
    i += 2;
  }
  if (n > largest) {
    largest = n;
  }
  return largest;
};
```