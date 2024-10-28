  let min_sum = Infinity;
  let current_sum = 0;

  for (const num of nums) {
    current_sum += num;
    min_sum = Math.min(min_sum, current_sum);
    if (current_sum > 0) {
      current_sum = 0;
    }
  }

  return min_sum;
}



