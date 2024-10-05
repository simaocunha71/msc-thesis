  let min = Infinity;
  let sum = 0;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    min = Math.min(min, sum);
    if (sum > 0) sum = 0;
  }

  return min;
}



