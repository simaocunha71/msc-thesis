  var sum = 0;

  for (const number of lst) {
    if (number > 0 && number % 2 != 0) {
      sum += number * number;
    }
  }

  return sum;
}