```js
const add = (lst) => {
  return lst.filter((n, i) => i % 2 !== 0 && n % 2 === 0).reduce((a, b) => a + b, 0)
}
```
