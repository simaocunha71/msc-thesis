  if (arr.length == 0) {
    return null;
  }

  let prod = 1;
  let sum = 0;
  for (const v of arr) {
    if (v < 0) {
      prod *= -1;
    } else if (v == 0) {
      return 0;
    }
    sum += Math.abs(v);
  }
  return prod * sum;
}

