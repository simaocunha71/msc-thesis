Here is a simple solution for this problem. We can use a single loop to iterate over the array and keep track of the minimum sum. We start with the minimum sum as the first element of the array. Then, for each subsequent element, we add it to the current sum and update the minimum sum if the new sum is less than the current minimum sum.

Here is the implementation in JavaScript:
```
const minSubArraySum = (nums) => {
  let minSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum += nums[i];
    minSum = Math.min(minSum, currentSum);
    if (currentSum < 0) {
      currentSum = 0;
    }
  }
  return minSum;
};
```
Here is how it works:

1. We initialize `minSum` as the first element of the array and `currentSum` as the first element of the array.
2. We iterate over the array starting from the second element.
3. For each element, we add it to `currentSum` and update `minSum` if the new sum is less than the current minimum sum.
4. If `currentSum` becomes negative, we reset it to 0 to avoid negative sums.
5. Finally, we return `minSum` as the minimum sum of any non-empty sub-array.

This solution has a time complexity of O(n), where n is the length of the array, because we only iterate over the array once. The space complexity is O(1) because we only use a constant amount of space to store the minimum sum and the current sum.