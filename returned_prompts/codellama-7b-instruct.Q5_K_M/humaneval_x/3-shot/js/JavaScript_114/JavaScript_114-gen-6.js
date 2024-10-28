  let current_sum = 0;
  let minimum_sum = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < nums.length; i++) {
    current_sum += nums[i];
    if (current_sum < minimum_sum) {
      minimum_sum = current_sum;
    }
    if (current_sum < 0) {
      current_sum = 0;
    }
  }

  return minimum_sum;
}



