  if (arr.length == 0) {
    return null;
  }

  let prod = 1;
  let sum = 0;

  for (const num of arr) {
    if (num < 0) {
      prod *= -1;
    } else if (num == 0) {
      prod = 0;
    }
    sum += Math.abs(num);
  }

  return prod * sum;
}