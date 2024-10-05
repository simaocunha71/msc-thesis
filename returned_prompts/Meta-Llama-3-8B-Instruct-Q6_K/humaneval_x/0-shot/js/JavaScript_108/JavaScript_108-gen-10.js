Here is a solution that uses a helper function to count the sum of digits of each number in the array:

```javascript
const countNums = (arr) => {
  const count = (num) => {
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
    return isNegative ? -sum : sum;
  };
  return arr.reduce((acc, curr) => (count(curr) > 0 ? acc + 1 : acc), 0);
};
```


In this solution, the `countNums` function iterates over each number in the input array `arr` using the `reduce` method. For each number, it calls the `count` helper function to calculate the sum of digits. If the sum is greater than 0, it increments the count. The `count` function checks if the number is negative and adjusts the sum accordingly. Finally, the `countNums` function returns the total count of numbers with a sum of digits greater than 0.