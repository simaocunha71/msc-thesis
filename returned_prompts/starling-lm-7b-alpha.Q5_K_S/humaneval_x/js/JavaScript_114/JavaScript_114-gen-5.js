  let min_sum = Number.POSITIVE_INFINITY;
  let current_sum = 0;

  for (const n of nums) {
    current_sum += n;
    if (current_sum < min_sum) {
      min_sum = current_sum;
    } else if (current_sum > 0) {
      current_sum = 0;
    }
  }

  return min_sum;
}



