/*
  Given an array of integers nums, find the minimum sum of any non-empty sub-array
  of nums.
  Example
  minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
  minSubArraySum([-1, -2, -3]) == -6
  */
const minSubArraySum = (nums) => {
  const arr = nums.slice();
  let subSum = +0;
  for (let i = 1; i < arr.length - 1; ++i) {
    subSum += arr[i] * (arr[i] > 0 ? 1 : -1);
  }
  return Math.min(subSum, 0);
};
module.exports = minSubArraySum;