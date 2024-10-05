To solve this problem, you can use Kadane's algorithm, which is a dynamic programming approach to find the maximum sum subarray in a given array.

Here's the implementation:

```javascript
const minSubArraySum = (nums) => {
  let minSum = nums[0];
  let currentMinSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentMinSum = Math.min(nums[i], currentMinSum + nums[i]);
    minSum = Math.min(minSum, currentMinSum);
  }

  return minSum;
};
```

Let's break down the code:

1. Initialize `minSum` and `currentMinSum` with the first element of the array.
2. Iterate through the array starting from the second element.
3. For each element, calculate `currentMinSum` as the minimum between the current element and the sum of the current element and `currentMinSum`.
4. Update `minSum` as the minimum between `minSum` and `currentMinSum`.
5. Finally, return `minSum`.

This algorithm runs in O(n) time complexity, where n is the length of the array.