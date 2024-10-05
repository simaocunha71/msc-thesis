```
function minSubArraySum(nums) {
  let minSum = Infinity;
  let currentSum = 0;

  for (let num of nums) {
    currentSum += num;
    minSum = Math.min(minSum, currentSum);
    if (currentSum > 0) {
      currentSum = 0;
    }
  }

  return minSum;
}
```

Explanation:

*   We initialize `minSum` to positive infinity and `currentSum` to 0.
*   We iterate through the array, adding each number to `currentSum` and updating `minSum` if `currentSum` is less than `minSum`.
*   If `currentSum` becomes positive, we reset it to 0 to start a new subarray sum.
*   The function returns `minSum`, which is the minimum sum of any non-empty subarray.

Example usage:
```
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // Output: 1
console.log(minSubArraySum([-1, -2, -3])); // Output: -6
```

This solution has a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1), as it only uses a constant amount of space to store the `minSum` and `currentSum` variables.