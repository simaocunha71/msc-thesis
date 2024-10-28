```javascript
const median = (l) => {
  return l.sort((a, b) => a - b)[Math.floor(l.length / 2)];
}
```
