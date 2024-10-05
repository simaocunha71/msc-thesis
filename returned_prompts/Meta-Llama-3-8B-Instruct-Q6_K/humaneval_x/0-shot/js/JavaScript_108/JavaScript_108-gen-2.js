Here is the solution for the problem:

```javascript
const countNums = (arr) => {
  let count = 0;
  for (let num of arr) {
    let sum = 0;
    let isNegative = false;
    if (num < 0) {
      isNegative = true;
      num = -num;
    }
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
};
```

This function goes through each number in the array. If the number is negative, it converts it to positive and sets a flag to indicate that it's negative. It then calculates the sum of the digits of the number. If the sum is greater than 0, it increments the count. Finally, it returns the count.