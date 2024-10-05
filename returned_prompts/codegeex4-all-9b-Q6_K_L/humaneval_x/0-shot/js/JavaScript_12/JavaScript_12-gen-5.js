```javascript
const longest = (strings) => {
  return strings.length === 0 ? null : strings.reduce((a, b) => a.length > b.length ? a : b);
}
```
