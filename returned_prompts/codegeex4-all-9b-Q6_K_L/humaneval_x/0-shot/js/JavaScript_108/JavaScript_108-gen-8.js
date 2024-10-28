```javascript
const countNums = (arr) => {
  let count = 0;
  for (let num of arr) {
    let sum = 0;
    let absNum = Math.abs(num);
    while (absNum > 0) {
      sum += absNum % 10;
      absNum = Math.floor(absNum / 10);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
};
```