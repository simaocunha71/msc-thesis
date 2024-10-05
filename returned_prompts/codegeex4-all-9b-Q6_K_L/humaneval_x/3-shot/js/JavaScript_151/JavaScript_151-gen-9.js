  var sum = 0;
  for (const n of lst) {
    if (n > 0 && Number.isInteger(n) && n % 2 == 1) {
      sum += n ** 2;
    }
  }
  return sum;
}



