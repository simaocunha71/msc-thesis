  if (arr.length == 0) {
    return null;
  }
  let prod = 1;
  let sum = 0;
  for (const i of arr) {
    if (i < 0) {
      prod *= -1;
    } else if (i > 0) {
      prod *= 1;
    }
    sum += Math.abs(i);
  }
  return prod * sum;
}