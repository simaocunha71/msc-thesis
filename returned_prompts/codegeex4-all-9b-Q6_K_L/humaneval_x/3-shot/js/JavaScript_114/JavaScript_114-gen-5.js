  let min = Infinity;

  for (let i = 0; i < nums.length; i++) {
    let sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum < min) {
        min = sum;
      }
    }
  }

  return min;
}



