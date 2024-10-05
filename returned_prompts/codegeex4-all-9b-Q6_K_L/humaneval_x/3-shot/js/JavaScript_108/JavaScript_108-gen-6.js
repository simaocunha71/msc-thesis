  var count = 0;
  for (var num of arr) {
    var sum = 0;
    var abs_num = Math.abs(num);
    while (abs_num > 0) {
      sum += abs_num % 10;
      abs_num = Math.floor(abs_num / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }
  return count;
}