```javascript
const rollingMax = (numbers) => {
  return numbers.map((num, i) => Math.max(...numbers.slice(0, i + 1)));
};
```
