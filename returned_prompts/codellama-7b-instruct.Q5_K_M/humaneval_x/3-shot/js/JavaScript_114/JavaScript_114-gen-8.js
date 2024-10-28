  var result = nums[0];
  var sum = 0;
  var i = 0;

  for (var j = 0; j < nums.length; j++) {
    sum += nums[j];
    while (sum > 0) {
      result = Math.min(result, sum);
      sum -= nums[i];
      i += 1;
    }
  }
  return result;
}



