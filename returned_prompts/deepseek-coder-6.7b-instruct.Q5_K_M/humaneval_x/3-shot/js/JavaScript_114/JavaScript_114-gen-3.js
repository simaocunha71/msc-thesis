  let min_sum = Infinity;
  let current_sum = 0;

  for  (let i = 0; i < nums.length; i++)  {
    current_sum += nums[i];
    if  (current_sum < min_sum)  {
      min_sum = current_sum;
    }
    current_sum = Math.min(current_tmp, nums[i]);
  }

  return min_sum;
}



