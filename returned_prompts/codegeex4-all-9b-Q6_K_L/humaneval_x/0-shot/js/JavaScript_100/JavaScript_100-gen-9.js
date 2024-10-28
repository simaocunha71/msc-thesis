```js
const makeAPile = (n) => {
  let res = [];
  let level = n;
  let stones = n;
  while (stones > 0) {
    res.push(level);
    stones -= level;
    level = stones % 2 === 0 ? stones + 1 : stones;
  }
  return res;
};
```