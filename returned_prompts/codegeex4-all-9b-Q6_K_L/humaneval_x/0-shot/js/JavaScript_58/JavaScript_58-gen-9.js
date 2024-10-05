```js
const common = (l1, l2) => {
  let set1 = new Set(l1);
  let set2 = new Set(l2);
  let common = [...set1].filter(x => set2.has(x));
  return [...new Set(common)].sort((a, b) => a - b);
}
```