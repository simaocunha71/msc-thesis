  let min_sum = Number.MAX_SAFE_INTEGER;
  let current_sum = 0;

  for (let i = 0; i < nums.length; i++) {
    current_sum += nums[i];
    while (current_sum < 0) {
      current_sum -= nums[i];
    }
    if (current_sum < min_sum) {
      min_sum = current_sum;
    }
  }

  return min_sum;
}



