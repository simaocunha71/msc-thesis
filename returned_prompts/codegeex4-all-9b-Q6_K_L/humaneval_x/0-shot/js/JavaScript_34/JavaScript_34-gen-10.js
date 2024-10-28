```js
const unique = (l) => {
  let seen = {};
  return l.filter(x => {
    if (seen[x]) return false;
    seen[x] = true;
    return true;
  });
}
```