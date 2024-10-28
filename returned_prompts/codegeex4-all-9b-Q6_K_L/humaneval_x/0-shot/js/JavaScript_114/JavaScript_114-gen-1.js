/*
  Given an array of integers nums, find the minimum sum of any non-empty sub-array
  of nums.
  Example
  minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
  minSubArraySum([-1, -2, -3]) == -6
  */
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  for (let i = 0; i < nums.length; i++) {
    let currSum = 0;
    for (let j = i; j < nums.length; j++) {
      currSum += nums[j];
      minSum = Math.min(minSum, currSum);
    }
  }
  return minSum;
};

console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // 1
console.log(minSubArraySum([-1, -2, -3])); // -6
