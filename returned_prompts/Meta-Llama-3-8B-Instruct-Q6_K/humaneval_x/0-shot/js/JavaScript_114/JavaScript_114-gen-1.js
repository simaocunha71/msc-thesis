You can solve this problem by using a sliding window approach. Initialize two pointers, start and end, to the start of the array. Initialize a variable sum to 0. Iterate over the array, and for each element, add it to sum. If sum is greater than the current minimum sum, update the minimum sum. If sum is greater than or equal to the target sum, move the start pointer to the right and subtract the element at the start pointer from sum. Return the minimum sum.

Here is the implementation in JavaScript:

```javascript
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let start = 0;
  let end = 0;
  let sum = 0;

  while (end < nums.length) {
    sum += nums[end];
    minSum = Math.min(minSum, sum);

    while (sum >= minSum && start <= end) {
      sum -= nums[start];
      start++;
    }
    end++;
  }
  return minSum;
};
```

This function works by iterating over the array and adding each element to the sum. If the sum is greater than the current minimum sum, it updates the minimum sum. If the sum is greater than or equal to the target sum, it moves the start pointer to the right and subtracts the element at the start pointer from the sum. This process continues until the end of the array is reached. The function returns the minimum sum.

For example, if you call `minSubArraySum([2, 3, 4, 1, 2, 4])`, the function will return 1, which is the minimum sum of any non-empty sub-array of the input array. If you call `minSubArraySum([-1, -2, -3])`, the function will return -6, which is the minimum sum of any non-empty sub-array of the input array.