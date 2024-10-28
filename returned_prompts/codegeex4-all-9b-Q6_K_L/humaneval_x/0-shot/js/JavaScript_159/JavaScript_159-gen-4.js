```js
const eat = (number, need, remaining) => {
  return [number + need, Math.max(0, remaining - need)];
}
```
