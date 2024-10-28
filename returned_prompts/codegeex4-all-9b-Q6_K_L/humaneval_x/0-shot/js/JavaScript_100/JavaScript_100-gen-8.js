```javascript
const makeAPile = (n) => {
  let pile = [];
  let current = n;
  for (let i = 0; i < n; i++) {
    pile.push(current);
    current += 2 * ((i % 2) ? 1 : -1);
  }
  return pile;
}
```