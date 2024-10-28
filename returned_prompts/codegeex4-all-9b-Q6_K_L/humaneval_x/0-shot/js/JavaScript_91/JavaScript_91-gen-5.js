```js
const isBored = (S) => {
  let split = S.split(/[.?!]/);
  return split.filter(x => x.startsWith('I')).length;
}
```