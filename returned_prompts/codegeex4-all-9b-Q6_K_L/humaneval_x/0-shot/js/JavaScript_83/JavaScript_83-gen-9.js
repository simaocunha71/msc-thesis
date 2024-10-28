```javascript
const startsOneEnds = (n) => {
  if (n === 1) return 2;
  if (n === 2) return 4;
  
  let count = 4;
  let base = 10 ** (n - 2);
  
  for (let i = 1; i < base; i++) {
    if (i.toString().startsWith('1') || i.toString().endsWith('1')) {
      count++;
    }
  }
  
  return count;
};
```
