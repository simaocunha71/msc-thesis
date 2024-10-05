  if (arr.length == 0) {
    return null;
  }
  let sign = 1;
  let sum = 0;
  for (const num of arr) {
    if (num != 0) {
      sign *= Math.sign(num);
      sum += Math.abs(num);
    }
  }
  return sign * sum;
}