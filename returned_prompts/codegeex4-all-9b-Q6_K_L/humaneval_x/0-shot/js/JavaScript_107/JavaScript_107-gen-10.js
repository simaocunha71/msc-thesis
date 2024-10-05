```js
const evenOddPalindrome = (n) => {
  let evens = 0;
  let odds = 0;
  for (let i = 1; i <= n; i++) {
    if (i.toString() === i.toString().split('').reverse().join('')) {
      if (i % 2 === 0) {
        evens++;
      } else {
        odds++;
      }
    }
  }
  return [evens, odds];
}
```
