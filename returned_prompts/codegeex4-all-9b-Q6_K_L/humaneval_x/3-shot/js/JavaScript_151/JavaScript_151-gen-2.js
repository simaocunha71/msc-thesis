  let sum = 0;
  for (const x of lst) {
    if (x > 0 && Number.isInteger(x)) {
      if (x % 2 == 1) {
        sum += x * x;
      }
    }
  }
  return sum;
}