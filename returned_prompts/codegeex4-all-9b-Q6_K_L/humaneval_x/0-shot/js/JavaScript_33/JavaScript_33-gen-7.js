```js
const sortThird = (l) => {
  return l.map((e, i) => {
    if (i % 3 === 0) {
      return [...new Set(l.filter((_, j) => j % 3 === 0))].sort((a, b) => a - b)[0];
    } else {
      return e;
    }
  });
}
```
