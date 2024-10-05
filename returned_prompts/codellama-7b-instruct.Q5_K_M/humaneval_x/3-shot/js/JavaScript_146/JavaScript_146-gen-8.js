  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10) {
      if (nums[i] % 10 > 5) {
        if (nums[i] % 100 < 10 || nums[i] % 100 > 90) {
          count++;
        }
      } else {
        if (nums[i] % 100 < 50 || nums[i] % 100 > 95) {
          count++;
        }
      }
    }
  }
  return count;
}



