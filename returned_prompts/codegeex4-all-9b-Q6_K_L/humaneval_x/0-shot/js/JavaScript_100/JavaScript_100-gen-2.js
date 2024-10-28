```js
const makeAPile = (n) => {
  let pile = [n];
  let next = n;
  let i = 1;
  while (i < n) {
    next = next + (n % 2 ? 2 : 1);
    pile.push(next);
    i++;
  }
  return pile;
}
```