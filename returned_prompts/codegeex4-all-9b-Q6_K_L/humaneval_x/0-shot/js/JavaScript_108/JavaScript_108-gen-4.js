```javascript
const countNums = (arr) => {
  const sumDigits = (num) => {
    let sum = 0;
    while (num !== 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    return sum;
  };
  return arr.filter(num => sumDigits(num) > 0).length;
}
```
