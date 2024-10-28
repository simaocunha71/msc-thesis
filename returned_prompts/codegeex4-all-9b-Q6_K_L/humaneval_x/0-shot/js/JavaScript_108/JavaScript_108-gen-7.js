```js
const countNums = (arr) => {
  if (arr.length === 0) return 0;
  return arr.filter(num => {
    let sum = 0;
    const str = num.toString();
    for (let i = 0; i < str.length; i++) {
      sum += parseInt(str[i], 10);
    }
    return sum > 0;
  }).length;
};
```
