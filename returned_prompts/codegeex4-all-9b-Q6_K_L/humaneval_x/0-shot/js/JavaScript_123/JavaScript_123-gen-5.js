```javascript
const getOddCollatz = (n) => {
  // If n is 1, return [1]
  if (n === 1) {
    return [1];
  }
  // If n is even, set next to n/2
  // If n is odd, set next to 3n+1
  let next = n % 2 === 0 ? n / 2 : 3 * n + 1;
  // If next is 1, return [1]
  if (next === 1) {
    return [1, n];
  }
  // Otherwise, return [1] and the result of getOddCollatz(next)
  return [1, n, ...getOddCollatz(next)];
}
```
