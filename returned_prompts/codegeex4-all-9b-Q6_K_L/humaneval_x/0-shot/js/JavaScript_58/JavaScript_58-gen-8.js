```javascript
const common = (l1, l2) => {
  return [...new Set(l1.filter(e => l2.includes(e)))].sort((a, b) => a - b);
}
```