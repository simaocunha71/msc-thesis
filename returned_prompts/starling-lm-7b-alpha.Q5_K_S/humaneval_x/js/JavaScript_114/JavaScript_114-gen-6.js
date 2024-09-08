  let result = Number.MAX_VALUE;
  for (let i = 0; i < nums.length; i++) {
    let current_sum = 0;
    for (let j = i; j < nums.length; j++) {
      current_sum += nums[j];
      result = Math.min(result, current_sum);
    }
  }
  return result;
}



