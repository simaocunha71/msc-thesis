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
}  // This function returns the minimum sum of any non-empty sub-array of nums. It iterates over the array and keeps track of the current sum. If the current sum is greater than 0, it resets it to 0. It also keeps track of the minimum sum seen so far. At the end of the iteration, it returns the minimum sum.
}  // This function returns the minimum sum of any non-empty sub-array of nums. It iterates over the array and keeps track of the current sum. If the current sum is greater than 0, it resets it to 0. It also keeps track of the minimum sum seen so far. At the end of the iteration, it returns the minimum sum.