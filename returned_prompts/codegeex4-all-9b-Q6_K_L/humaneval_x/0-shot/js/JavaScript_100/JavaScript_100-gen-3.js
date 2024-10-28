```js
const makeAPile = (n) => {
  let pile = [];
  let i = 0;
  while (i < n) {
    pile.push(n + 2 * i);
    i++;
  }
  return pile;
}
```
