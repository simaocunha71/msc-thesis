  let sum = nums[0], minSum = nums[0];
  for(let i = 1; i < nums.length; i++) {
    sum = Math.min(nums[i], sum + nums[i]);
    minSum = Math.min(minSum, sum);
  }
  return minSum;
}



