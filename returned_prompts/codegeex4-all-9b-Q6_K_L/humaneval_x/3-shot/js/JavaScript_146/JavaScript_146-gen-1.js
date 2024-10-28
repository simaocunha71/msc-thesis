  var count = 0;
  for (var i = 0; i < nums.length; i++) {
    if (nums[i] > 10) {
      var str = nums[i].toString();
      if ((str[0] % 2 == 1) && (str[str.length - 1] % 2 == 1)) {
        count += 1;
      }
    }
  }
  return count;
}

