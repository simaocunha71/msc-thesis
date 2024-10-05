```js
  const levels = [];
  let stones = n;
  while (stones > 0) {
    levels.push(stones);
    stones += n % 2 === 0 ? 2 : 1;
  }
  return levels;
}
```