  var result = 0;

  for (var i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && (nums[i] % 10 == 1 || nums[i] % 10 == 3 || nums[i] % 10 == 5 || nums[i] % 10 == 7 || nums[i] % 10 == 9)) {
      result++;
    }
  }

  return result;
}



