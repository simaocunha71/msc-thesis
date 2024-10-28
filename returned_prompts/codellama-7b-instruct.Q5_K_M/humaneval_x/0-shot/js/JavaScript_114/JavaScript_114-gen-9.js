const minSubArraySum = (nums) => {
  let minSum = nums[0];
  let sum = 0;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    minSum = Math.min(minSum, sum);
    if (sum < 0) {
      sum = 0;
    }
  }
  return minSum;
};
