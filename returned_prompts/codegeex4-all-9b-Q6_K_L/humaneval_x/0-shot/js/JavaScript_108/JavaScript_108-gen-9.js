```js
const countNums = (arr) => {
  return arr.filter(x => {
    let sum = 0;
    let xStr = x.toString();
    for (let i = 0; i < xStr.length; i++) {
      sum += Number(xStr[i]);
    }
    return sum > 0;
  }).length;
}
```