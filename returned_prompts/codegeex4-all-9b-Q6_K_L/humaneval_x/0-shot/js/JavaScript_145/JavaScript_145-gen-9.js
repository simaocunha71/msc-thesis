```javascript
const orderByPoints = (nums) => {
  let digitsSum = (num) => {
    let numStr = Math.abs(num).toString();
    let sum = 0;
    for (let i = 0; i < numStr.length; i++) {
      sum += parseInt(numStr[i]);
    }
    return sum;
  };
  return nums.sort((a, b) => digitsSum(a) - digitsSum(b));
};
```
