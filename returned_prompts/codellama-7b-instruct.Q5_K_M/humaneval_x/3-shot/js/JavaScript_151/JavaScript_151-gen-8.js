  var sum = 0;
  for (const num of lst) {
    if (Number.isInteger(num) && num >= 0) {
      if (num % 2 == 1) {
        sum += num * num;
      }
    }
  }
  return sum;
}



