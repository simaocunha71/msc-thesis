To solve this problem, we can follow these steps:

1. Initialize a variable, minSum, to store the minimum sum of the sub-array, and set it to positive infinity. This ensures that any sum will be smaller than positive infinity.

2. Use two pointers, start and end, to keep track of the start and end of the sub-array. Initially, set start to 0 and end to 0.

3. Initialize a variable, sum, to store the sum of the current sub-array. Set sum to nums[0].

4. Use a while loop to iterate until end is less than nums.length - 1. Within the loop, perform the following steps:

   a. Add nums[end] to sum.

   b. Check if sum is less than minSum. If true, update minSum with sum.

   c. If sum is greater than the target sum (sum of all elements), reset sum to nums[end] and increment start by 1. This is because the current sub-array sum is not meeting the target sum, so we need to find a new sub-array sum by sliding the start pointer.

   d. Increment end by 1.

5. After the while loop, return minSum as the minimum sum of any non-empty sub-array of nums.

This algorithm has a time complexity of O(n), where n is the length of the nums array, as we only iterate through the array once.

The space complexity is O(1), as we only use a constant amount of extra space to store variables.

*/

const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let start = 0;
  let end = 0;
  let sum = nums[0];

  while (end < nums.length) {
    sum += nums[end];
    while (sum > nums.length && start < end) {
      sum -= nums[start];
      start += 1;
    }
    if (sum < minSum) {
      minSum = sum;
    }
    end += 1;
  }

  return minSum;
};

console.log