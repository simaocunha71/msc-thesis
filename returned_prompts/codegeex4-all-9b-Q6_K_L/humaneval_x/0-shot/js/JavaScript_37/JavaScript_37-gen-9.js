```js
const sortEven = (l) => {
  let l2 = l.map((x, i) => i % 2 ? x : l.filter((y, j) => j % 2 == 0).sort((a, b) => a - b)[Math.floor(i / 2)]);
  return l2;
}
```