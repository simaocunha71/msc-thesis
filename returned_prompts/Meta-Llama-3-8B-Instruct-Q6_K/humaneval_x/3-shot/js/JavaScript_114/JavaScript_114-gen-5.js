  let min_sum = Infinity;
  for (let i = 0; i < nums.length; i++) {
    let current_sum = 0;
    for (let j = i; j < nums.length; j++) {
      current_sum += nums[j];
      min_sum = Math.min(min_sum, current_sum);
    }
  }
  return min_sum;
}