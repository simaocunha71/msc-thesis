```js
const largestPrimeFactor = (n) => {
  let largest = 2;
  while (n > largest) {
    if (n % largest === 0) {
      n /= largest;
    } else {
      largest++;
    }
  }
  return largest;
}
```