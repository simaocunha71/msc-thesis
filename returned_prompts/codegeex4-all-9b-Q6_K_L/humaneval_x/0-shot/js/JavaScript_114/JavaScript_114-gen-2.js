The problem requires finding the minimum sum of any non-empty sub-array from a given array of integers. This can be efficiently solved using Kadane's Algorithm, which is designed to find the maximum sum sub-array in a given array. However, for the minimum sum, we can modify the algorithm slightly. 

Here is the implementation of the minSubArraySum function:

```javascript
const minSubArraySum = (nums) => {
  if (nums.length === 0) return 0;
  let minSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.min(nums[i], currentSum + nums[i]);
    minSum = Math.min(minSum, currentSum);
  }

  return minSum;
}
```

In this solution:
1. We initialize minSum and currentSum with the first element of the array since that's the minimum we know so far.
2. We iterate through the rest of the array.
3. For each element, we update currentSum to be the minimum of the current element itself or the sum of the current element and the previous currentSum. This ensures that we are always considering the minimum possible sub-array sum up to that point.
4. We update minSum to be the minimum of the current minSum and the updated currentSum.
5. Finally, we return minSum, which holds the minimum sum of any non-empty sub-array.

This solution has a time complexity of O(n), where n is the number of elements in the array, because it only requires a single pass through the array.