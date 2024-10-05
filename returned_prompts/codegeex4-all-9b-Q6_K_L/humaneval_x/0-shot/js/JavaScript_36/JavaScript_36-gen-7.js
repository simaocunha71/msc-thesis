```js
const fizzBuzz = (n) => {
  return [...Array(n).keys()].filter((i) => i % 11 === 0 || i % 13 === 0)
    .map((i) => String(i))
    .reduce((acc, cur) => acc + (cur.match(/7/g) || []).length, 0);
};
```