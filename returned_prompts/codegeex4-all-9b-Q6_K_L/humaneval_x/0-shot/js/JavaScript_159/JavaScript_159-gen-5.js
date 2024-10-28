```js
const eat = (number, need, remaining) => {
  var eaten = number + need;
  var left = remaining - need;
  return [eaten, left < 0 ? 0 : left];
}
```