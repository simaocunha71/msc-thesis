  let sum = 0;
  for (let num of lst) {
    if (Math.floor(num) === num && num > 0) {
      sum += num ** 2;
    }
  }
  return sum;
}