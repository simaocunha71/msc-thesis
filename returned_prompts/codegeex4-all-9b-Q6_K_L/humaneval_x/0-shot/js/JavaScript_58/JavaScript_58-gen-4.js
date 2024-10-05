```javascript
const common = (l1, l2) => {
  const set1 = new Set(l1);
  const set2 = new Set(l2);
  const result = [...new Set([...set1].filter(x => set2.has(x)))];
  return result.sort((a, b) => a - b);
}
```
