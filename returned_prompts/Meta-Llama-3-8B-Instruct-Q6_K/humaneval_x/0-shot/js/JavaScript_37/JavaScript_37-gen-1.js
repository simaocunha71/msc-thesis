```javascript
const sortEven = (l) => {
  return l.map((val, idx) => idx % 2 === 0 ? [...l.slice(0, idx), ...l.slice(idx + 1)].sort((a, b) => a - b).slice(0, 1)[0] : val);
};
```