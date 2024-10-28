  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && (nums[i] % 10) % 2 != 0) {
      count++;
    }
  }
  return count;
}



