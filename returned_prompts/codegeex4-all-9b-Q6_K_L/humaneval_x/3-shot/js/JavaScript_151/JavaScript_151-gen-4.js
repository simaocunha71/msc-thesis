  var sum = 0;
  for (var num of lst) {
    if (num % 2 == 1 && num >= 0 && num % 1 == 0) {
      sum += num * num;
    }
  }
  return sum;
}



