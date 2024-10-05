```js
const countNums = (arr) => {
  return arr.reduce((count, num) => {
    const absNum = Math.abs(num);
    const sum = absNum.toString().split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    return count + (sum > 0 ? 1 : 0);
  }, 0);
}
```