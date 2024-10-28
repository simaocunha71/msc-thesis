```js
const pairsSumToZero = (l) => {
  const set = new Set();
  for (const num of l) {
    if (set.has(-num)) return true;
    set.add(num);
  }
  return false;
}
```