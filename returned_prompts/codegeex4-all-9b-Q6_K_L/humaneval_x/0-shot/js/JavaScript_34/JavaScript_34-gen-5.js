```javascript
const unique = (l) => {
  const seen = new Set();
  return l.filter(x => !seen.has(x) && seen.add(x));
}
```