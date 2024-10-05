This problem can be solved by iterating over the array and keeping track of the minimum sum of any non-empty sub-array.

Here is the JavaScript solution:

```javascript
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let currentSum = 0;

  for (let i = 0; i < nums.length; i++) {
    currentSum += nums[i];

    minSum = Math.min(minSum, currentSum);

    if (currentSum > 0) {
      currentSum = 0;
    }
  }

  return Math.min(minSum, currentSum);
};
```

This function initializes two variables, `minSum` and `currentSum`, to keep track of the minimum sum and the current sum of the sub-array, respectively. It then iterates over the array, adding each element to `currentSum` and updating `minSum` if `currentSum` is less than `minSum`. If `currentSum` becomes greater than 0, it is reset to 0. Finally, the function returns the minimum of `minSum` and the current sum, which is the minimum sum of any non-empty sub-array.

For example, for the input `[2, 3, 4, 1, 2, 4]`, the function will return `1`, which is the minimum sum of any non-empty sub-array. For the input `[-1, -2, -3]`, the function will return `-6`, which is the minimum sum of any non-empty sub-array.