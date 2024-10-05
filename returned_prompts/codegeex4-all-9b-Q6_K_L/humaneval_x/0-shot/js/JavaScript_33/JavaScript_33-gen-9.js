```js
const sortThird = (l) => {
  let modThree = l.filter((_, i) => i % 3 === 0);
  modThree.sort((a, b) => a - b);
  return l.map((item, index) => (index % 3 === 0 ? modThree.shift() : item));
}
```
