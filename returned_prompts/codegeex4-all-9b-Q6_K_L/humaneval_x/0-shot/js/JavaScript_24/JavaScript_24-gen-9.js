```js
const largestDivisor = (n) => {
  for (let i = Math.floor(Math.sqrt(n)); i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
}
```