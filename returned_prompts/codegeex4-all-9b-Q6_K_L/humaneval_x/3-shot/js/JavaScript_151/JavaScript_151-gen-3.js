  var sum = 0;
  for (const n of lst) {
    if (n > 0 && n % 2 == 1 && Number.isInteger(n)) {
      sum += n * n;
    }
  }
  return sum;
}