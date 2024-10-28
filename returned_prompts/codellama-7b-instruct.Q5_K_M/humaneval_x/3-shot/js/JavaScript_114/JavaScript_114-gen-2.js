  let min_sum = Number.MAX_SAFE_INTEGER;
  let current_sum = 0;

  for (let i = 0; i < nums.length; i++) {
    current_sum += nums[i];
    min_sum = Math.min(current_sum, min_sum);
    if (current_sum < 0) {
      current_sum = 0;
    }
  }

  return min_sum;
}



