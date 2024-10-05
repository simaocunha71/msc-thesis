```javascript
const stringSequence = (n) => {
  if (n === 0) return '0';
  let sequence = '';
  for (let i = 0; i <= n; i++) {
    sequence += i;
    if (i < n) sequence += ' ';
  }
  return sequence;
}
```
