  let result = Infinity;
  for (let i = 0; i < nums.length; i++) {
    let current_sum = 0;
    for (let j = i; j < nums.length; j++) {
      current_sum += nums[j];
      if (current_sum < result) {
        result = current_sum;
      }
    }
  }
  return result;
}



