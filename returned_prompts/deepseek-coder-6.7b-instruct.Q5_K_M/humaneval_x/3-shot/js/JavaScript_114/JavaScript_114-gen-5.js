  let min = nums[0];
  let current = nums[0];

  for (let i = 1; i < nums.length; i++) {
    current = Math.min(nums[i], current + nums[i]);
    min = Math.min(min, current);
  }

  return min;
}



