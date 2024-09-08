  if (arr.length === 0) {
    return null;
  }

  let sign = 1;
  let sum = 0;

  for (const n of arr) {
    if (n === 0) {
      sign *= 0;
    } else if (n > 0) {
      sign *= 1;
    } else {
      sign *= -1;
    }
    sum += Math.abs(n);
  }

  return sign * sum;
}



