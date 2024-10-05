The problem is to find the minimum sum of any non-empty sub-array of a given array of integers. The brute force approach would involve checking all possible sub-arrays, which would be computationally expensive for large arrays.

Instead, we can use Kadane's algorithm, which is an efficient algorithm to find the maximum sum sub-array in linear time. We can adapt this algorithm to find the minimum sum sub-array by taking the negative of the maximum sum sub-array. Here's how we can implement this in JavaScript:

```javascript
const minSubArraySum = (nums) => {
  let currentSum = nums[0];
  let minSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    minSum = Math.min(minSum, currentSum);
  }

  return minSum;
};
```

This implementation initializes the currentSum and minSum variables with the first element of the array. Then, it iterates through the array, updating the currentSum and minSum variables based on the maximum and minimum sub-array sums found so far.

The time complexity of this implementation is O(n), where n is the length of the input array, because it only requires a single pass through the array. The space complexity is O(1) because it only uses a constant amount of extra space.