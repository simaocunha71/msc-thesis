  let min = 0;
  for (let i = 0; i < nums.length; i++) {
    min += nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      min = Math.min(min, min + nums[j]);
    }
  }
  return min;
}
