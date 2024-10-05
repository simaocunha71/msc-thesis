```js
const makeAPile = (n) => {
  if (n === 0) return [];
  const arr = [n];
  let nextLevel = n % 2 === 0 ? n + 1 : n + 2;
  while (nextLevel <= 2 * n) {
    arr.push(nextLevel);
    nextLevel = nextLevel % 2 === 0 ? nextLevel + 1 : nextLevel + 2;
  }
  return arr;
};
```
