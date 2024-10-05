  const minSubArraySum = (nums) => {
    let minSum = 0;
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
      sum += nums[i];
      if (sum < minSum || minSum === 0) {
        minSum = sum;
      }
      if (sum < 0) {
        sum = 0;
      }
    }
    return minSum;
  };
  return minSubArraySum;

