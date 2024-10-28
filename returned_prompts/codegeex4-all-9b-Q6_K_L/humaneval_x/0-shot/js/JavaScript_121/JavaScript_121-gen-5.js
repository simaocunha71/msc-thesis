```js
const solution = (lst) => {
  return lst.reduce((acc, el, i) => {
    if (i % 2 === 0 && el % 2 !== 0) acc += el;
    return acc;
  }, 0);
}
```
