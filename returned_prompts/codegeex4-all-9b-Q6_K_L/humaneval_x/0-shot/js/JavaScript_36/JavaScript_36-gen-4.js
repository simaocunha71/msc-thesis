```javascript
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 0; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      let str = i.toString();
      for (let j = 0; j < str.length; j++) {
        if (str[j] === '7') {
          count++;
        }
      }
    }
  }
  return count;
}
```
