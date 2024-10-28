  var min_sum = nums[0];
  var current_sum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    current_sum = Math.min(current_sum + nums[i], nums[i]);
    min_sum = Math.min(min_sum, current_sum);
  }

  return min_sum;
}



