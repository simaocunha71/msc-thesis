  var count = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && (nums[i] % 10).toString()[0] % 2 == 1 && (nums[i] % 10).toString()[1] % 2 == 1) {
      count++;
    }
  }
  return count;
}



