```js
const iscube = (a) => {
  if (a === 0) {
    return true;
  }
  if (a < 0) {
    a = -a;
  }
  const root = Math.floor(Math.pow(a, 1 / 3));
  return Math.pow(root, 3) === a;
}
```