  let min_sum = 0;
  let current_sum = 0;

  for (const num of nums) {
    current_sum += num;
    if (current_sum < min_sum) {
      min_sum = current_sum;
    }
  }

  return min_sum;
}



