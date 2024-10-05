```js
const iscube = (a) => {
  if(a === 0) return true;
  let cube = Math.abs(a) ** (1/3);
  return cube === Math.floor(cube);
}
```
