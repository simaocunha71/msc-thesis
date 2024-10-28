  let min_sum = Infinity;
  let current_sum = 0;

  for (let i = 0; i < nums.length; i++) {
    current_sum = Math.min(current_sum + nums[i], nums[i]);
    min_sum = Math.min(min_sum, current_sum);
  }

  return min_sum;
}



