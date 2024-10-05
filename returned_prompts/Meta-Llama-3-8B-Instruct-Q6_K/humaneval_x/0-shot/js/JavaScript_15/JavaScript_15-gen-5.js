```javascript
const stringSequence = (n) => {
  const numbers = [];
  for (let i = 0; i <= n; i++) {
    numbers.push(i.toString());
  }
  return numbers.join(' ');
};
``` 