  var sum = 0;
  for (const number of lst) {
    if (number % 1 == 0 && number > 0 && number % 2 == 1) {
      sum += number * number;
    }
  }
  return sum;
}