```javascript
const sortThird = (l) => {
  return l.map((x, i) => {
    if (i % 3 === 0) {
      return [...new Set(l.filter((_, j) => j % 3 === 0))].sort((a, b) => a - b)[0];
    }
    return x;
  });
};
```
