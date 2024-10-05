```js
const countNums = (arr) => {
  const sumDigits = (num) => {
    let sum = 0;
    let absNum = Math.abs(num);
    while (absNum > 0) {
      sum += absNum % 10;
      absNum = Math.floor(absNum / 10);
    }
    return num < 0 ? -sum : sum;
  };
  return arr.filter(num => sumDigits(num) > 0).length;
}
```
