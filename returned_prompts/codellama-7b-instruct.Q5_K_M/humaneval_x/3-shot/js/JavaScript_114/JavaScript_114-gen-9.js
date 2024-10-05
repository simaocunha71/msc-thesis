  var min_sum = Number.MAX_VALUE;

  for (let i = 0; i < nums.length; i++) {
    var sum = 0;

    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum < min_sum) {
        min_sum = sum;
      }
    }
  }

  return min_sum;
}



