```js
const sortThird = (l) => {
  const thirdIndices = l.filter((_, i) => i % 3 === 0);
  thirdIndices.sort((a, b) => a - b);
  return l.map((_, i) => (i % 3 === 0 ? thirdIndices[i / 3] : l[i]));
}
```
