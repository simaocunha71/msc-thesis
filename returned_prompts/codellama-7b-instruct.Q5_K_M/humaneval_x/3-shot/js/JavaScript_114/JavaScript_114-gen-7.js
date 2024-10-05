  var min_sum = Number.POSITIVE_INFINITY;
  var current_sum = 0;

  for (let i = 0; i < nums.length; i++) {
    current_sum += nums[i];
    if (current_sum < min_sum) {
      min_sum = current_sum;
    }

    current_sum = Math.max(current_sum - nums[i], 0);
  }

  return min_sum;
}



