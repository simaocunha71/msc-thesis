/*
  Given an array of integers nums, find the minimum sum of any non-empty sub-array
  of nums.
  Example
  minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
  minSubArraySum([-1, -2, -3]) == -6
  */
const minSubArraySum = (nums) => {
  let minSum = Infinity, sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    minSum = Math.min(minSum, sum);
    if (sum < 0) {
      sum = 0;
    }
  }
  return minSum;
}
