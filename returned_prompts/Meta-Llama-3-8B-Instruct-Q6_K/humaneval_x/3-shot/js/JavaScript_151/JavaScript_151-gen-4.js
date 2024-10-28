  let sum = 0;
  for (let num of lst) {
    if (typeof num == 'number' && num >= 0 && num % 1 == 0 && num % 2 != 0) {
      sum += num ** 2;
    }
  }
  return sum;
}
