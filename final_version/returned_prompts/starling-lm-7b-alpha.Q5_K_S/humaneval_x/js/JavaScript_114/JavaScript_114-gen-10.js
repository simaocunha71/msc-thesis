  let min_sum = Infinity;
  let curr_sum = 0;

  for (let i = 0; i < nums.length; i++) {
    curr_sum += nums[i];
    if (curr_sum < min_sum) {
      min_sum = curr_sum;
    } else if (curr_sum < 0) {
      curr_sum = 0;
    }
  }

  return min_sum;
}



