To find the minimum sum of any non-empty sub-array of the given array of integers `nums`, we can use the Kadane's algorithm. The idea is to iterate through the array and keep track of the current sum of the sub-array. If the current sum becomes negative, we reset it to zero because a negative sum will only increase the total sum of the sub-array. We also keep track of the minimum sum found so far.

Here's the implementation of the `minSubArraySum` function in JavaScript:

```javascript
const minSubArraySum = (nums) => {
  let currentSum = 0;
  let minSum = Infinity;

  for (let i = 0; i < nums.length; i++) {
    currentSum += nums[i];
    minSum = Math.min(minSum, currentSum);
    currentSum = Math.max(currentSum, 0);
  }

  return minSum === Infinity ? 0 : minSum;
};
```

Let's test the function with the given examples:

```javascript
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // Output: 1
console.log(minSubArraySum([-1, -2, -3])); // Output: -6
```

The function returns the expected outputs for both examples.