  var min_sum = Number.MAX_SAFE_INTEGER;

  for (var i = 0; i < nums.length; i++) {
    var sum = 0;
    for (var j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum < min_sum) {
        min_sum = sum;
      }
    }
  }

  return min_sum;
}



