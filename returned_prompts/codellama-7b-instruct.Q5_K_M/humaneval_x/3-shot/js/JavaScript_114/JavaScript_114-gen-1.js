  let min_sum = 0;
  let current_sum = 0;
  for (let i = 0; i < nums.length; i++) {
    current_sum += nums[i];
    if (i == 0 || current_sum < min_sum) {
      min_sum = current_sum;
    }
    if (current_sum < 0) {
      current_sum = 0;
    }
  }

  return min_sum;
}



