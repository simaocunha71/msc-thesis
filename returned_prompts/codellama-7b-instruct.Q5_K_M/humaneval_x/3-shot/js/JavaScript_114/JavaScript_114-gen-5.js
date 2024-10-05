  var result = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < nums.length; i++) {
    var sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum < result) {
        result = sum;
      }
    }
  }

  return result;
}



