Here's one way to implement the `minSubArraySum` function in JavaScript:

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

  return minSum === Infinity ? 0 : minSum;
};
```

This function iterates through the input array `nums` and keeps track of the current sum of elements and the minimum sum found so far. If the current sum becomes greater than 0, it resets the current sum to 0 because a subarray with a sum of 0 would be better. Finally, it returns the minimum sum found, or 0 if no valid subarray exists.