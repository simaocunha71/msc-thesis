```javascript
const sortThird = (l) => {
  const indicesToSort = l.filter((_, i) => i % 3 === 0);
  indicesToSort.sort((a, b) => a - b);
  return l.map((x, i) => i % 3 === 0 ? indicesToSort.shift() : x);
}
```