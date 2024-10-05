  if (!arr.length) return null;

  let prod = 1;
  let sum = 0;

  for (let num of arr) {
    if (num !== 0) {
      sum += Math.abs(num);
      prod *= Math.sign(num);
    }
  }

  return prod * sum;
}